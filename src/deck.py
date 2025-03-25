
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
    
    def __str__(self):
        return f"Carta añadida: {self.cards}"