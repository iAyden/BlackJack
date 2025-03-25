class Card:
    def __init__(self,value,color,suits):
        self.value = value
        self.color = color
        self.suits= suits
    
    def __str__(self):
        return f"{self.value } with color {self.color} and suit {self.suits}  "

print(Card(10,"red","diamond"))



   # def insert_value(self, value):
