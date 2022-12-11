from dice import Dice

class Weapon:

    def __init__(self, dice, num_rolls, name, rarity, cost):
        self._dice = dice
        self.num_rolls = num_rolls
        self.name = name
        self.rarity = rarity
        self.cost = cost

    @property
    def damage(self):
        return self._dice.roll(self.num_rolls)

    def __repr__(self):
        return f"\n{self.name}, damage: {self.num_rolls}d{self._dice}, rarity: {self.rarity}, cost: {self.cost}"

weapons = [
    Weapon(Dice(6), 1, "Long sword", 0.5, 100),
    Weapon(Dice(6), 2, "Wolf Knight's Greatsword", 0.8, 800),
    Weapon(Dice(12), 1, "Uchigatana", 0.6, 500),
    Weapon(Dice(4), 2, "Sellsword Twinblades", 0.5, 200),
    Weapon(Dice(4), 1, "Dagger", 0.4, 50)
]

if __name__ == "__main__":
    weapons[0].cost = 1
    print(weapons[0])
