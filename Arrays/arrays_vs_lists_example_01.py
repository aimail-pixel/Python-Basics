"Core Basics example: Arrays vs lists (1)"

def main():
    from array import array
    a = array("i", [2, 4])
    print(a.tolist(), a.typecode)


if __name__ == "__main__":
    main()
