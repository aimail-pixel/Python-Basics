"Core Basics example: Lambda (1)"

def main():
    rows = [("A", 3), ("B", 1)]
    print(sorted(rows, key=lambda row: row[1]))


if __name__ == "__main__":
    main()
