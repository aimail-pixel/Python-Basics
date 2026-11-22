"Core Basics example: Set methods (2)"

def main():
    a = {1, 2, 3}
    a.intersection_update({2, 4})
    print(sorted(a))


if __name__ == "__main__":
    main()
