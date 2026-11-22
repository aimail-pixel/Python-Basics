"Core Basics example: Removing values (2)"

def main():
    from array import array
    a = array("i", range(5))
    print(a.pop())
    del a[:2]
    print(a.tolist())


if __name__ == "__main__":
    main()
