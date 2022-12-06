import random


def run_world():
    creatures = [50] * 10
    names = [f"creature_{i}" for i in range(10)]
    # names = ["creature_" + str(i) for i in range(10)]

    # while len(creatures) > 1:
    while True:
        num = len(creatures)
        for i in range(num):
            j = random.randint(0, num - 1)
            if i == j:
                continue
            creatures[j] -= random.randint(0, 10)

        # same!
        creatures_temp = []
        names_temp = []
        for i in range(len(creatures)):
            if creatures[i] > 0:
                creatures_temp.append(creatures[i])
                names_temp.append(names[i])
        creatures = creatures_temp
        names = names_temp

        print(creatures, names)

        if len(creatures) <= 1:
            break


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
            # print("Self harm!")
            return
        other.health -= random.randint(0, 5)
        if other.health <= 0:
            self.exp += 200
        # receive_exp here if killed other

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
    id = 1  # class variable

    def __init__(self):
        self.name = f"world_{World.id}"  # instance variable
        World.id += 1

        self.creatures = [Creature() for _ in range(10)]

    def __repr__(self) -> str:
        strs = [f"\t{cr}" for cr in self.creatures]
        creatures_str = "\n".join(strs)

        # same:
        # creatures_str = "\n".join(str(cr) for cr in self.creatures)
        return f"World [name: {self.name}, creatures: [\n{creatures_str}\n]"

    def tick(self) -> None:
        for creature in self.creatures:
            creature.lvl_up()
            creature.attack(random.choice(self.creatures))

        self.creatures = [cr for cr in self.creatures if cr.health > 0]
        for creature in self.creatures:
            creature.exp += 100

        # receive_exp here for survivors

    def run(self):
        while len(self.creatures) > 1:
            self.tick()


if __name__ == "__main__":


    # creature = Creature()
    # creature - экземпляр класса
    # Creature - класс в целом
    # creature.health  # значение поля экземпляра
    # other = Creature()
    # creature.attack(other)  # вызов метода для экземпляра класса
    # вместо self подставляется creature (в методе attack)

    # Creature.attack(other)
    #
    # print(Creature.creatures_created())
    # print(Creature.version())
    # print(creature.version())

    ws = [World() for _ in range(5)]
    for w in ws:
        print("========")
        print(w)
        print("")
        w.run()
        print(w)

# Ctrl - посмотреть объявление
# Ctrl + space - подсказка ввода
# Ctrl + / - закомментировать и откомментировать строку
# Выделить строки + Tab -  увеличить индентацию
# Выделить строки + Shift + Tab - уменьшить индентацию
# Ctrl + Alt + L - автоформаттер кода
