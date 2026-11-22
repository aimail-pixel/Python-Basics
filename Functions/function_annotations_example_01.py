"Core Basics example: Function annotations (1)"

def main():
    def twice(n: int) -> int:
        return n * 2
    print(twice(3))


if __name__ == "__main__":
    main()
