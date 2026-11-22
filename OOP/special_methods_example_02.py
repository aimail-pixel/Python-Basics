"Core Basics example: Special methods (2)"

def main():
    class Coins:
        def __init__(self, n): self.n = n
        def __add__(self, other):
            if not isinstance(other, Coins):
                return NotImplemented
            return Coins(self.n + other.n)
    print((Coins(2) + Coins(3)).n)


if __name__ == "__main__":
    main()
