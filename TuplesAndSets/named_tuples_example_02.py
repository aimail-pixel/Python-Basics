"Core Basics example: Named tuples (2)"

def main():
    from collections import namedtuple
    Seat = namedtuple("Seat", "row number")
    print(Seat("A", 2)._replace(number=3))


if __name__ == "__main__":
    main()
