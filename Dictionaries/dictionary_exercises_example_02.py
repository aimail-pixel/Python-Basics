"Core Basics example: Dictionary exercises (2)"

def main():
    seats = {"Ada": 1, "Roy": 2}
    print({v: k for k, v in seats.items()})


if __name__ == "__main__":
    main()
