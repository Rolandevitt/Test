from world import World


if __name__ == "__main__":

    ws = [World() for _ in range(5)]
    for w in ws:
        print("========")
        print(w)
        print("")
        w.run()
        print(w)
