"Core Basics example: Removing values (1)"

def main():
    from array import array
    a = array("i", [1, 2, 1])
    a.remove(1)
    print(a.tolist())


if __name__ == "__main__":
    main()
