from dice import Dice

class Weapon:

    def __init__(self, damage, name, rarity, cost):
        self.damage = damage
        self.name = name
        self.rarity = rarity
        self.cost = cost

    def __repr__(self):
        return f"\n{self.name} deals damage {self.damage}, rarity: {self.rarity}, cost: {self.cost}"

weapons = [
    Weapon(Dice(1, 6).show_dice(), "Long sword", 0.5, 100),
    Weapon(Dice(2, 6).show_dice(), "Wolf Knight's Greatsword", 0.8, 800),
    Weapon(Dice(1, 12).show_dice(), "Uchigatana", 0.6, 500),
    Weapon(Dice(2, 4).show_dice(), "Sellsword Twinblades", 0.5, 200),
    Weapon(Dice(1, 4).show_dice(), "Dagger", 0.4, 50)
]

print(weapons)


