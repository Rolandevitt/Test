import random
from weapon import *


class Creature:
    id = 1

    def __init__(self):
        self.health = 25
        self.name = f"creature_{Creature.id}"
        self.ac = 11  # armor class
        self.exp = 0
        self.lvl = 1
        self.weapon = weapons[random.randint(0, (len(weapons) - 1))]
        self.dmg = self.weapon.damage()
        Creature.id += 1

    @classmethod
    def creatures_created(cls) -> int:
        return cls.id - 1

    @staticmethod
    def version() -> str:
        return "1.0.0"

    def _is_enemy(self, other):
        return other != self

    def attack(self, other):
        hit = Dice(20).roll()
        if hit >= other.ac:
            if self.health > 0:
                other.health -= self.dmg
                if other.health <= 0:
                    self.exp += 200
        if hit == 1:
            self.health -= 1

    def lvl_up(self):
        if self.exp >= 1000 and self.lvl < 2:
            self.lvl = 2
            self.health += random.randint(1, 6)
        if self.exp >= 3000 and self.lvl < 3:
            self.lvl = 3
            self.health += random.randint(1, 6)

    def __repr__(self) -> str:
        return f"\nCreature [name: {self.name}, health: {self.health}, lvl: {self.lvl}," \
               f" exp: {self.exp}, weapon: {self.weapon}]"


class Monster(Creature):
    id = 1

    def __init__(self):
        super().__init__()
        self.name = f"monster_{Monster.id}"
        self.health = random.randint(10, 15)
        Monster.id += 1

    def lvl_up(self):
        pass

    def __repr__(self) -> str:
        return f"\nMonster [name: {self.name}, health: {self.health}, weapon: {self.weapon}]"


class Fighter(Creature):
    id = 1

    def __init__(self):
        super().__init__()
        self.name = f"fighter_{Fighter.id}"
        self.health = random.randint(5, 15)
        self.dex = random.randint(1, 3)
        self.ac = armors[random.randint(0, (len(armors) - 1))].base_ac + self.dex
        Fighter.id += 1

    def __repr__(self) -> str:
        return f"\nFighter [name: {self.name}, health: {self.health}, lvl: {self.lvl}, exp: {self.exp}, " \
               f"weapon: {self.weapon.name} with damage: {self.weapon.num_rolls}d{self.weapon.dice}] "


if __name__ == "__main__":
    print([Monster() for _ in range(10)])
    print([Fighter() for _ in range(5)])
