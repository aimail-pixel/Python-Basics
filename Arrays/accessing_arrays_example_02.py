"Core Basics example: Accessing arrays (2)"

def main():
    from array import array
    a = array("d", [1, 2])
    a[0] = 1.5
    print(a.tolist())


if __name__ == "__main__":
    main()
