"Core Basics example: Remove items (2)"

def main():
    a = [10, 20, 30, 40]
    print(a.pop())
    del a[:2]
    print(a)


if __name__ == "__main__":
    main()
