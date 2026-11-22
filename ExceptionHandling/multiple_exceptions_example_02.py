"Core Basics example: Multiple exceptions (2)"

def main():
    try:
        print(int(None))
    except (TypeError, ValueError):
        print("Cannot convert")


if __name__ == "__main__":
    main()
