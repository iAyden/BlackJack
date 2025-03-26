class Player:
    def __init__(self,id):
        self.id = id
        self.hand = []

    def insert_card(self,id,card):
        self.hand.append(card)

    def get_sumhand(self):
        return sum(self.hand)
    
    def is_empty(self):
        if self.hand == 0 or None:
            return not self.hand
        else:
            return True

    def delete_card(self, index):
        if self.is_empty():
            raise Exception("Array is empty")
        self.hand.pop(index)

    def create_new_hand(self,id):
        if id == 0 or None:
            raise Exception("Id cannot be 0 or None")
        else:
            Player(id)

    def print_hand(self,id):
        for card in self.hand:
            print(f"Cards of player{card}")

    def get_hand(self):
        return self.hand