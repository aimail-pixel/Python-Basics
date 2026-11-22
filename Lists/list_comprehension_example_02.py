"Core Basics example: List comprehension (2)"

def main():
    names = ["Ada", "", "Roy"]
    print([s.upper() for s in names if s])


if __name__ == "__main__":
    main()
