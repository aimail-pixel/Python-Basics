"Core Basics example: with open() lifecycle (2)"

def main():
    try:
        with open("sample.txt", "w", encoding="utf-8") as f:
            raise ValueError("stop")
    except ValueError:
        print("Closed:", f.closed)


if __name__ == "__main__":
    main()
