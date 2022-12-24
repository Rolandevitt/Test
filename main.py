from world import World


if __name__ == "__main__":

    ws = [World() for _ in range(5)]
    for w in ws:
        print("========")
        print(f"WORLD {ws.index(w)+1}")
        w.run()
        print(w)
