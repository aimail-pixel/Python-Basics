"Core Basics example: Sort (2)"

def main():
    names = ["tea", "fig", "apricot"]
    print(sorted(names, key=len, reverse=True))


if __name__ == "__main__":
    main()
