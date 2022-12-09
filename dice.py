import random

class Dice:

    def __init__(self, num, sides):
        self.num = num
        self.sides = sides
    def roll(self):
        self.result = 0
        for _ in range(self.num):
            self.result = self.result + random.randint(1, self.sides)
        return self.result
    def show_dice(self) -> str:
        return f"{self.num}d{self.sides}"

    def __repr__(self):
        return f"{self.roll()}"


if __name__ == "__main__":
    dc = [Dice(3, 6) for _ in range(5)]
    for d in dc:
        print("=======")
        print(d)




