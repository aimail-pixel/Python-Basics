"Core Basics example: Practical validation (1)"

def main():
    import re
    for pin in ["700150", "70015x"]:
        print(pin, bool(re.fullmatch(r"[1-9][0-9]{5}", pin)))


if __name__ == "__main__":
    main()
