"Core Basics example: Default arguments (1)"

def main():
    def greet(name="Guest"):
        return f"Hello {name}"
    print(greet(), greet("Ada"))


if __name__ == "__main__":
    main()
