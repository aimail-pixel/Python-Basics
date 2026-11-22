"Core Basics example: Instance, class & static methods (1)"

def main():
    class Box:
        def __init__(self, size):
            self.size = size
        @classmethod
        def unit(cls):
            return cls(1)
        def volume(self):
            return self.size ** 3
    print(Box.unit().volume())


if __name__ == "__main__":
    main()
