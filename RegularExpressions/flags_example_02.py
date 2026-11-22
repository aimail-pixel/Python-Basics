"Core Basics example: Flags (2)"

def main():
    import re
    print(bool(re.fullmatch("a.b", "a\nb", re.S)))


if __name__ == "__main__":
    main()
