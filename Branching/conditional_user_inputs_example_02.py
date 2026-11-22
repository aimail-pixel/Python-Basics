"Core Basics example: Conditional user inputs (2)"

def main():
    try:
        age = int(input())
        print("Adult" if age >= 18 else "Minor")
    except ValueError:
        print("Enter a whole number")


if __name__ == "__main__":
    main()
