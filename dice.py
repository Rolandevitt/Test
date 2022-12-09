import random

class Dice:

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
       return random.randint(1, self.sides)

d20 = Dice(20)
d12 = Dice(12)
d10 = Dice(10)
d8 = Dice(8)
d6 = Dice(6)
d4 = Dice(4)


if __name__ == "__main__":
    print(d20.roll())       #Test
    print(d4.roll())
    print(d8.roll())
    print(d10.roll())
