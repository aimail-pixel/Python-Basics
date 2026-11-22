"Core Basics example: Metacharacters (1)"

def main():
    import re
    print(re.findall(r"c[au]t", "cat cot cut"))


if __name__ == "__main__":
    main()
