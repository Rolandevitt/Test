import random
from creature import Fighter, Monster


class World:
    id = 1

    def __init__(self):
        self.name = f"world_{World.id}"
        World.id += 1

        self.monsters = [Monster() for _ in range(5)]
        self.fighters = [Fighter() for _ in range(5)]

    def __repr__(self) -> str:
        strs = "\n".join(str(monster) for monster in self.monsters)
        fighters = "\n".join(str(fighter) for fighter in self.fighters)

        return f"World [name: {self.name},\n\tmonsters: [\n{strs}\n\tfighters: [\n{fighters}\n]"

    def tick(self) -> None:
        for fighter in self.fighters:
            if len(self.fighters) > 0:
                fighter.attack(random.choice(self.monsters))

        self.monsters = [monster for monster in self.monsters if monster.health > 0]
        print(self.monsters)

        for monster in self.monsters:
            if len(self.monsters) > 0:
                monster.attack(random.choice(self.fighters))

        self.fighters = [fighter for fighter in self.fighters if fighter.health > 0]

        for fighter in self.fighters:
            fighter.exp += 100
            fighter.lvl_up()

        # print(self.monsters)

    def run(self):
        while len(self.monsters) > 0 and len(self.fighters) > 0:
            self.tick()
        if len(self.monsters) == 0:
            print("Fighters win!")
        else:
            print("Monsters win!")
