"Core Basics example: Copy (2)"

def main():
    a = [[1]]
    b = a.copy()
    b[0].append(2)
    print(a)


if __name__ == "__main__":
    main()
