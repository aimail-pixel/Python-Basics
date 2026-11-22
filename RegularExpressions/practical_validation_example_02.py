"Core Basics example: Practical validation (2)"

def main():
    import re
    for code in ["PY-012", "PY-12"]:
        print(code, bool(re.fullmatch(r"[A-Z]{2}-[0-9]{3}", code)))


if __name__ == "__main__":
    main()
