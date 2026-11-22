"Core Basics example: else & finally (1)"

def main():
    for text in ("3", "x"):
        try:
            n = int(text)
        except ValueError:
            print("Bad input")
        else:
            print(n * 2)
        finally:
            print("Done")


if __name__ == "__main__":
    main()
