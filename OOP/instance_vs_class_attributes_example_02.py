"Core Basics example: Instance vs class attributes (2)"

def main():
    class Bag:
        def __init__(self):
            self.items = []
    a, b = Bag(), Bag()
    a.items.append("pen")
    print(a.items, b.items)


if __name__ == "__main__":
    main()
