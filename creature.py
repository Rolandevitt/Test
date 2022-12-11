import random
from weapon import *

class Creature:
    id = 1

    def __init__(self):
        self.health = 50
        self.name = f"creature_{Creature.id}"
        self.exp = 0
        self.lvl = 1
        Creature.id += 1
        self.weapon = weapons[random.randint(0, (len(weapons) - 1))]

    @classmethod
    def creatures_created(cls) -> int:
        return cls.id - 1

    @staticmethod
    def version() -> str:
        return "1.0.0"

    def _is_enemy(self, other):
        return other != self

    def attack(self, other: "Creature") -> None:
        if not self._is_enemy(other):
            return
        other.health -= self.weapon.damage
        if other.health <= 0:
            self.exp += 100

    def lvl_up(self):
        if self.exp >= 1000 and self.lvl < 2:
            self.lvl = 2
            self.health += random.randint(1, 10)
        if self.exp >= 3000 and self.lvl < 3:
            self.lvl = 3
            self.health += random.randint(11, 25)

    def __repr__(self) -> str:
        return f"\nCreature [name: {self.name}, health: {self.health}, lvl: {self.lvl}, exp: {self.exp}, weapon: {self.weapon}]"


class Fighters(Creature):
    def __int__(self):
        super().__init__()

    def _is_enemy(self, other):
        return not isinstance(other, Fighters)

    def __repr__(self) -> str:
        return f"\nFighter [name: {self.name}, health: {self.health}, lvl: {self.lvl}, exp: {self.exp}, weapon: {self.weapon}]"



if __name__ == "__main__":
    print([Creature() for _ in range (5)])
    print([Fighters() for _ in range (5)])