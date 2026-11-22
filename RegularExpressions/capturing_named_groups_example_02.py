"Core Basics example: Capturing & named groups (2)"

def main():
    import re
    m = re.search(r"(ab)(?:cd)", "xxabcd")
    print(m.group(0), m.group(1), m.span(1))


if __name__ == "__main__":
    main()
