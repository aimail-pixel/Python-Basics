"Core Basics example: Set operators (1)"

def main():
    a, b = {1, 2}, {2, 3}
    print(sorted(a | b), sorted(a & b))


if __name__ == "__main__":
    main()
