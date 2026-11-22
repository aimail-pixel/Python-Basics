"Core Basics example: finditer() (1)"

def main():
    import re
    for m in re.finditer(r"\w+", "hi all"):
        print(m.group(), m.span())


if __name__ == "__main__":
    main()
