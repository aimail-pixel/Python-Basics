"Core Basics example: raise & custom exceptions (1)"

def main():
    def check(n):
        if n < 0:
            raise ValueError("Negative count")
    try:
        check(-1)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
