import random

class Creature:
    id = 1

    def __init__(self):
        self.health = 50
        self.name = f"creature_{Creature.id}"
        self.exp = 0
        self.lvl = 1
        Creature.id += 1

    @classmethod
    def creatures_created(cls) -> int:
        return cls.id - 1

    @staticmethod
    def version() -> str:
        return "1.0.0"

    def attack(self, other: "Creature") -> None:
        if other == self:
            return
        other.health -= random.randint(0, 5)
        if other.health <= 0:
            self.exp += 200

    def lvl_up(self):
        if self.exp >= 1000 and self.lvl < 2:
            self.lvl = 2
            self.health += random.randint(1, 5)
        if self.exp >= 3000 and self.lvl < 3:
            self.lvl = 3
            self.health += random.randint(1, 10)

    def __repr__(self) -> str:
        return f"Creature [name: {self.name}, health: {self.health}, lvl: {self.lvl}, exp: {self.exp}]"