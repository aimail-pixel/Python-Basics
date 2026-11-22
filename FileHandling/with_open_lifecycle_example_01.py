"Core Basics example: with open() lifecycle (1)"

def main():
    with open("sample.txt", "w", encoding="utf-8") as f:
        print(f.closed)
    print(f.closed)


if __name__ == "__main__":
    main()
