"Core Basics example: split() (2)"

def main():
    import re
    print(re.split(r"(-)", "A-B-C", maxsplit=1))


if __name__ == "__main__":
    main()
