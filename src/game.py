from card import Card 
from deck import Deck
from player import Player

d = Deck()
player = Player(1)
dealer = Player(2)
def create_cards_for_deck():
    Color = ["red","black"]
    Suit = ["heart", "diamond", "club", "spade"]
    print(Suit[:2])
    y = 1
    i = 1
    
    for y in Suit[:2]:
        for i in range(2,10):
            c = Card(i,Color[0],y)
            d.add_card(c)
        
        for i in range(4):
            c = Card(10,Color[0],y)
            d.add_card(c)
        c = Card(11,Color[0],y)
        d.add_card(c)

    for y in Suit[2:]:
        for i in range(2,10):
            c = Card(i,Color[1],y)
            d.add_card(c)
        for i in range(4):
            c = Card(10,Color[1],y)
            d.add_card(c)
            c = Card(11,Color[1],y)
            d.add_card(c)
    d.print_deck()
    

def give_cards_to_player():
    first_card = d.get_random_card()
    second_card = d.get_random_card()
    player.insert_card(first_card)
    player.insert_card(second_card)
    player.print_hand()
    return player.get_hand()

def give_cards_to_dealer():
    first_card = d.get_random_card()
    second_card = d.get_random_card()
    dealer.insert_card(first_card)
    dealer.insert_card(second_card)
    dealer.print_hand()
    return dealer.get_hand()

def hit_card_player():
    card = d.get_random_card()
    player.insert_card(card)
    player.print_hand()
    return player.get_hand()

def hit_card_dealer():
    card = d.get_random_card()
    dealer.insert_card(card)
    dealer.print_hand()
    return dealer.get_hand()

def check_if_bust_twentyone(total):
    if total >21:
        return False
    else:
        True
def check_winner(dealer_total,player_total):
    if dealer_total<player_total:  
        if player_total>21:
            return False
        else:
            return True
    elif player_total<dealer_total:
        if dealer_total>21:
            return True
        else:
            return False
    
def reset_deck():
    d.clear_deck()
    create_cards_for_deck()
    player.clear_hand()
    dealer.clear_hand()
#d.print_deck()


