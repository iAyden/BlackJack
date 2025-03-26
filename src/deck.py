import random
class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self,card):
        if not self.cards:
            self.cards.append(card)
            return
        if not card in self.cards:
            self.cards.append(card)
        else:
            return f"Error, card exists in Deck"
        
    def print_deck(self):
        for card in self.cards:
            print(card)
    
    def is_empty(self):
        if len(self.cards) == None:
            return True
        else:
            return False
        
    def get_random_card(self):
      
        random_card = random.choice(self.cards)
        self.remove_card(random_card)
        return random_card
        
    def remove_card(self,card):
        if self.is_empty() == True:
            raise Exception("Deck is empty")
        else:
            self.cards.remove(card) 

    def __str__(self):
        return f"Carta añadida: {self.cards}"