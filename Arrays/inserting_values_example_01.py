"Core Basics example: Inserting values (1)"

def main():
    from array import array
    a = array("i", [2, 6])
    a.insert(1, 4)
    print(a.tolist())


if __name__ == "__main__":
    main()
