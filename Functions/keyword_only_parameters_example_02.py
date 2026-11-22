"Core Basics example: Keyword-only parameters (2)"

def main():
    def label(name, *, upper=False):
        return name.upper() if upper else name
    print(label("tea", upper=True))


if __name__ == "__main__":
    main()
