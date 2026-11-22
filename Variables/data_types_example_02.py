"Core Basics example: Data types (2)"

def main():
    def length(value):
        return len(value) if isinstance(value, str) else 0
    print(length("Kolkata"), length(7))


if __name__ == "__main__":
    main()
