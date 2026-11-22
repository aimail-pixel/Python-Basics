"Core Basics example: Inserting values (2)"

def main():
    from array import array
    a = array("f", [1])
    a.append(2.5)
    a.extend([3, 4])
    print(a.tolist())


if __name__ == "__main__":
    main()
