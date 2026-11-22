"Core Basics example: Multiple exceptions (1)"

def main():
    for s in ("bad", "0"):
        try:
            print(10 / int(s))
        except ValueError:
            print("Invalid integer")
        except ZeroDivisionError:
            print("Zero divisor")


if __name__ == "__main__":
    main()
