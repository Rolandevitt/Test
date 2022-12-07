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


class World:
    id = 1

    def __init__(self):
        self.name = f"world_{World.id}"
        World.id += 1

        self.creatures = [Creature() for _ in range(10)]

    def __repr__(self) -> str:
        strs = [f"\t{cr}" for cr in self.creatures]
        creatures_str = "\n".join(strs)

        return f"World [name: {self.name}, creatures: [\n{creatures_str}\n]"

    def tick(self) -> None:
        for creature in self.creatures:
            creature.attack(random.choice(self.creatures))

        self.creatures = [cr for cr in self.creatures if cr.health > 0]
        for creature in self.creatures:
            creature.exp += 100
            creature.lvl_up()

    def run(self):
        while len(self.creatures) > 1:
            self.tick()


if __name__ == "__main__":


    ws = [World() for _ in range(5)]
    for w in ws:
        print("========")
        print(w)
        print("")
        w.run()
        print(w)

