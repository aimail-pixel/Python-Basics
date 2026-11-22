"Core Basics example: Keyword-only parameters (1)"

def main():
    def price(n, *, tax):
        return n + tax
    print(price(20, tax=3))


if __name__ == "__main__":
    main()
