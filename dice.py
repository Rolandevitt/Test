import random

class Dice:

    def __init__(self, sides):
        self.sides = sides

    def roll(self, num = 1):
        result = 0
        for _ in range(num):
            result = result + random.randint(1, self.sides)
        return result

    def __repr__(self):
        return f"{self.sides}"


if __name__ == "__main__":
    dc = [Dice(6) for _ in range(5)]
    for d in dc:
        print("=======")
        print(d.roll())




