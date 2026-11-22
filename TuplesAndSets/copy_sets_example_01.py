"Core Basics example: Copy sets (1)"

def main():
    a = {1}
    b = a.copy()
    b.add(2)
    print(sorted(a), sorted(b))


if __name__ == "__main__":
    main()
