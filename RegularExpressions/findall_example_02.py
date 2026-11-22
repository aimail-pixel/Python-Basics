"Core Basics example: findall() (2)"

def main():
    import re
    print(re.findall(r"([A-Z])(\d)", "A1 B2"))


if __name__ == "__main__":
    main()
