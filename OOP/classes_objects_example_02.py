"Core Basics example: Classes & objects (2)"

def main():
    class Seat:
        pass
    a, b = Seat(), Seat()
    a.row, b.row = "A", "B"
    print(a.row, b.row, a is b)


if __name__ == "__main__":
    main()
