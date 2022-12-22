import json


class Weapon:

    def __init__(self, dice, num_rolls, name, cost):
        self.dice = dice
        self.num_rolls = num_rolls
        self.name = name
        self.cost = cost

    def damage(self):
        return self.dice.roll(self.num_rolls)

    def __repr__(self):
        return f"\n{self.name}, damage: {self.num_rolls}d{self.dice}, cost: {self.cost}"


# weapons = [
#     Weapon(6, 1, "Long sword", 100),
#     Weapon(6, 2, "Wolf Knight's Greatsword", 800),
#     Weapon(12, 1, "Uchigatana", 500),
#     Weapon(4, 2, "Sellsword Twinblades", 200),
#     Weapon(4, 1, "Dagger", 50)
# ]
config = {"weapons": [
        {"dice": 6, "num_rolls": 1, "name": "Long sword", "cost": 100},
        {"dice": 6, "num_rolls": 2, "name": "Wolf Knight's Greatsword", "cost": 800},
        {"dice": 12, "num_rolls": 1, "name": "Uchigatana", "cost": 500},
        {"dice": 4, "num_rolls": 2, "name": "Sellsword Twinblades", "cost": 200},
        {"dice": 4, "num_rolls": 1, "name": "Dagger", "cost": 50}
    ]},
{"armors": [
        {"base_ac": 11, "weight": "light", "name": "Leather armor"},
        {"base_ac": 13, "weight": "medium", "name": "Chain shirt"},
        {"base_ac": 15, "weight": "medium", "name": "Half plate"},
        {"base_ac": 18, "weight": "heavy", "name": "Plate armor"}
    ]}


# weapons = json.loads(weapons_json)

with open('config.json', 'w') as file:
    json.dump(config, file, indent=2)


class Armor:

    def __init__(self, base_ac, category, name):
        self.base_ac = base_ac
        self.category = category
        self.name = name

    def __repr__(self):
        return f"\n{self.name}, base AC = {self.base_ac}"


if __name__ == "__main__":
    with open('config.json') as file:
        data = json.load(file)
        print(data(["weapons"][0]["name"]))
        a = {"s": 1, "a": 2}
        print(data.items())