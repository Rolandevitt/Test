import json
from dice import Dice

with open('config.json') as file:
    data = json.load(file)

class Weapon:

    def __init__(self, num):
        self.dice = Dice(data["weapons"][num]["dice"])
        self.num_rolls = data["weapons"][num]["num_rolls"]
        self.name = data["weapons"][num]["name"]
        self.cost = data["weapons"][num]["cost"]

    def damage(self):
        return self.dice.roll(self.num_rolls)

    def __repr__(self):
        return f"\n{self.name}, damage: {self.num_rolls}d{self.dice}, cost: {self.cost}"


class Armor:

    def __init__(self, num):
        self.base_ac = data["armors"][num]["base_ac"]
        self.weight = data["armors"][num]["weight"]
        self.name = data["armors"][num]["name"]

    def __repr__(self):
        return f"\n{self.name} ({self.weight}), base AC = {self.base_ac}"


if __name__ == "__main__":
    print("")
