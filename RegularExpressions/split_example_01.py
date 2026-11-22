"Core Basics example: split() (1)"

def main():
    import re
    print(re.split(r"[,;]\s*", "a,b; c"))


if __name__ == "__main__":
    main()
