"Core Basics example: Syntax vs runtime errors (2)"

def main():
    try:
        print(2 / 0)
    except ZeroDivisionError:
        print("Division failed")


if __name__ == "__main__":
    main()
