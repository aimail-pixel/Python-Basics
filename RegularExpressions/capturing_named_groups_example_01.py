"Core Basics example: Capturing & named groups (1)"

def main():
    import re
    m = re.fullmatch(r"(?P<city>[A-Z]+)-(?P<id>\d+)", "CCU-42")
    print(m.groupdict())


if __name__ == "__main__":
    main()
