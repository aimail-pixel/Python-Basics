"Core Basics example: Tuple unpacking (2)"

def main():
    first, *middle, last = (2, 4, 6, 8)
    print(first, middle, last)


if __name__ == "__main__":
    main()
