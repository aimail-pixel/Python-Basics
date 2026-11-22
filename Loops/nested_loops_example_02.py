"Core Basics example: Nested loops (2)"

def main():
    for height in range(1, 4):
        row = ""
        for _ in range(height):
            row += "*"
        print(row)


if __name__ == "__main__":
    main()
