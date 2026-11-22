"Core Basics example: Dictionary comprehensions (2)"

def main():
    words = ["tea", "apple", "fig"]
    print({w: len(w) for w in words if len(w) == 3})


if __name__ == "__main__":
    main()
