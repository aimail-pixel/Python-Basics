"Core Basics example: Encapsulation & property (1)"

def main():
    class Square:
        def __init__(self, side):
            self._side = side
        @property
        def area(self):
            return self._side ** 2
    print(Square(3).area)


if __name__ == "__main__":
    main()
