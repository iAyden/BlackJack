class Card:
    def __init__(self,value,color,suits):
        if (0<value<=11):
            self.value = value
        else:
            print(f" The value {value} is not valid it must be between 0-10")
            return None
        if color in ("red", "black"): #if self.color == "red" or self.color == "black" 
            self.color = color
        else:
            print(f"The color {color} is not valid it must be red or black")
            return None
        if suits in ("heart", "diamond", "club", "spade"):
            self.suits= suits
        else:
            print(f"The suit {suits} is not valid, it must be diamond, club, heart or spade")
            return None

    def __str__(self):
        return f"{self.value },{self.color},{self.suits}"





   # def insert_value(self, value):
