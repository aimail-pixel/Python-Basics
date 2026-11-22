"Core Basics example: sub() (2)"

def main():
    import re
    print(re.sub(r"\d+", lambda m: str(int(m[0]) * 2), "x3 y4"))


if __name__ == "__main__":
    main()
