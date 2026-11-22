"Core Basics example: Positional-only parameters (2)"

def main():
    def convert(n, /, *, unit):
        return f"{n} {unit}"
    print(convert(7, unit="km"))


if __name__ == "__main__":
    main()
