"Core Basics example: Set exercises (1)"

def main():
    registered, present = {"Ada", "Roy"}, {"Roy"}
    print(sorted(registered - present))


if __name__ == "__main__":
    main()
