"Core Basics example: Dictionary methods (1)"

def main():
    d = {"a": 1}
    keys = d.keys()
    d.update(b=2)
    print(list(keys))


if __name__ == "__main__":
    main()
