"Core Basics example: Dictionary methods (2)"

def main():
    groups = {}
    for word in ["ant", "ape", "bee"]:
        groups.setdefault(word[0], []).append(word)
    print(groups)


if __name__ == "__main__":
    main()
