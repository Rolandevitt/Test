import random
from creature import Creature

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