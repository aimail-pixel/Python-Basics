"Core Basics example: Walrus operator (2)"

def main():
    words = ["a", "tea", "water"]
    print([n for w in words if (n := len(w)) > 2])


if __name__ == "__main__":
    main()
