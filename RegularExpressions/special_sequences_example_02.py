"Core Basics example: Special sequences (2)"

def main():
    import re
    print(bool(re.fullmatch(r"\d\s\d", "2\t7")))


if __name__ == "__main__":
    main()
