"Core Basics example: Named tuples (1)"

def main():
    from collections import namedtuple
    Point = namedtuple("Point", "x y")
    p = Point(3, 4)
    print(p.x, p[1])


if __name__ == "__main__":
    main()
