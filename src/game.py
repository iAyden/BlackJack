from card import Card 
from deck import Deck

d = Deck()


Color = ["red","black"]
Suit = ["heart", "diamond", "club", "spade"]
x = 0
y = 1
i = 1
for x in Color:
    for y in Suit:
        for i in range(1,10):
            c = Card(i,x,y)
            response = d.add_card(c)
        for i in range(4):
            c = Card(10,x,y)
            response = d.add_card(c)
        c = Card(11,x,y)
        response = d.add_card(c)
d.print_deck()




    