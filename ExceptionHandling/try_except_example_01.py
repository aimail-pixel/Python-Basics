"Core Basics example: try & except (1)"

def main():
    try:
        n = int("many")
        print(n)
    except ValueError:
        print("Enter digits")


if __name__ == "__main__":
    main()
