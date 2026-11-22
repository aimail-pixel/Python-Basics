"Core Basics example: Tuple exercises (1)"

def main():
    players = (("A", 7), ("B", 9))
    name, score = max(players, key=lambda p: p[1])
    print(name, score)


if __name__ == "__main__":
    main()
