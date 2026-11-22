"Core Basics example: Add to sets (2)"

def main():
    s = {"red"}
    s.update(["red", "blue"])
    print(sorted(s))


if __name__ == "__main__":
    main()
