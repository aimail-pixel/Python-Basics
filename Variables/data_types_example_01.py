"Core Basics example: Data types (1)"

def main():
    for item in (7, "7", [7], {"n": 7}):
        print(type(item).__name__)


if __name__ == "__main__":
    main()
