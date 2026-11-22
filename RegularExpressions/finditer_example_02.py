"Core Basics example: finditer() (2)"

def main():
    import re
    print(sum(1 for _ in re.finditer("aa", "aaaaa")))


if __name__ == "__main__":
    main()
