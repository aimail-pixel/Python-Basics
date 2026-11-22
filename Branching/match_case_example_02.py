"Core Basics example: match-case (2)"

def main():
    point = (0, 5)
    match point:
        case (0, y) if y > 0:
            print("Positive y-axis", y)
        case _:
            print("Elsewhere")


if __name__ == "__main__":
    main()
