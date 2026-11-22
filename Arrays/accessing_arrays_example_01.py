"Core Basics example: Accessing arrays (1)"

def main():
    from array import array
    a = array("i", [4, 6, 8])
    print(a[-1], a[:2].typecode)


if __name__ == "__main__":
    main()
