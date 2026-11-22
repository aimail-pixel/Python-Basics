"Core Basics example: search() (2)"

def main():
    import re
    m = re.search("blue", "red")
    print(m.group() if m else "Missing")


if __name__ == "__main__":
    main()
