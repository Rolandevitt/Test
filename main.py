from world import World
from dice import *

if __name__ == "__main__":

    ws = [World() for _ in range(5)]
    for w in ws:
        print("========")
        print(w)
        print("")
        w.run()
        print(w)

        print(f" roll_d20: {d20.roll()}")  #Test Dice
        print(f" roll_d6: {d6.roll()}")
        print(f" roll_d4: {d4.roll()}")

