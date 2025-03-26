from card import Card 
from deck import Deck
from player import Player

d = Deck()
player = Player(1)
dealer = Player(2)
def create_cards_for_deck():
    Color = ["red","black"]
    Suit = ["heart", "diamond", "club", "spade"]
    x = 0
    y = 1
    i = 1
    for x in Color:
        for y in Suit:
            for i in range(1,10):
                c = Card(i,x,y)
                d.add_card(c)
            for i in range(4):
                c = Card(10,x,y)
                d.add_card(c)
            c = Card(11,x,y)
            d.add_card(c)
    d.print_deck()

def give_cards_to_player():
    first_card = d.get_random_card()
    second_card = d.get_random_card()
    player.insert_card(1,first_card)
    player.insert_card(1,second_card)
    player.print_hand(1)
    


#d.print_deck()



    