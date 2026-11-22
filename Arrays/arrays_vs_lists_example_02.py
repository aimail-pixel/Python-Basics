"Core Basics example: Arrays vs lists (2)"

def main():
    mixed = [3, "three"]
    print([type(x).__name__ for x in mixed])


if __name__ == "__main__":
    main()
