"Core Basics example: Converting arrays (2)"

def main():
    from array import array
    a = array("i", [4, 8])
    b = array("i")
    b.frombytes(a.tobytes())
    print(b == a)


if __name__ == "__main__":
    main()
