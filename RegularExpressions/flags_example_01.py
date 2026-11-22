"Core Basics example: Flags (1)"

def main():
    import re
    print(re.findall("^go", "Go\nGO", re.I | re.M))


if __name__ == "__main__":
    main()
