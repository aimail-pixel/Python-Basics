"Core Basics example: Positional-only parameters (1)"

def main():
    def scale(value, /, factor=2):
        return value * factor
    print(scale(5, factor=3))


if __name__ == "__main__":
    main()
