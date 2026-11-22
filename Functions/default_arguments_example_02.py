"Core Basics example: Default arguments (2)"

def main():
    def collect(x, items=None):
        if items is None:
            items = []
        items.append(x)
        return items
    print(collect(1), collect(2))


if __name__ == "__main__":
    main()
