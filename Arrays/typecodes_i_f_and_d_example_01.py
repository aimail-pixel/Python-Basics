"Core Basics example: Typecodes i, f and d (1)"

def main():
    from array import array
    for code in "ifd":
        print(code, array(code).itemsize, "bytes")


if __name__ == "__main__":
    main()
