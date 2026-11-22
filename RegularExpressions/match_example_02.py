"Core Basics example: match() (2)"

def main():
    import re
    print(bool(re.match(r"\d+", "12a")), bool(re.fullmatch(r"\d+", "12a")))


if __name__ == "__main__":
    main()
