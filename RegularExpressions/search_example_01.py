"Core Basics example: search() (1)"

def main():
    import re
    m = re.search(r"\d+", "item 27")
    print(m.group(), m.span())


if __name__ == "__main__":
    main()
