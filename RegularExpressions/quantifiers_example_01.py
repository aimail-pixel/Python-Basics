"Core Basics example: Quantifiers (1)"

def main():
    import re
    print(re.findall(r"\b\d{2,3}\b", "1 22 333 4444"))


if __name__ == "__main__":
    main()
