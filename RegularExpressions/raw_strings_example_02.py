"Core Basics example: Raw strings (2)"

def main():
    import re
    print(re.findall(r"\bcat\b", "cat catalog"))


if __name__ == "__main__":
    main()
