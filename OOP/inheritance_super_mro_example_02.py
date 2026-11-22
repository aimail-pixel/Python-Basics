"Core Basics example: Inheritance, super() & MRO (2)"

def main():
    class Root: pass
    class Left(Root): pass
    class Right(Root): pass
    class Leaf(Left, Right): pass
    print([c.__name__ for c in Leaf.__mro__])


if __name__ == "__main__":
    main()
