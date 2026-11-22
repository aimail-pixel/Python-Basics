"Core Basics example: Set exercises (2)"

def main():
    groups = [{"art", "code"}, {"code", "math"}, {"code"}]
    print(sorted(set.intersection(*groups)))


if __name__ == "__main__":
    main()
