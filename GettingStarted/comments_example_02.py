"Core Basics example: Comments (2)"

def main():
    def square(n):
        """Return the square of n."""
        return n * n
    print(square.__doc__)


if __name__ == "__main__":
    main()
