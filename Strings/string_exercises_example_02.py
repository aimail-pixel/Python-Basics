"Core Basics example: String exercises (2)"

def main():
    phrase = "Never odd or even"
    clean = phrase.replace(" ", "").casefold()
    print(clean == clean[::-1])


if __name__ == "__main__":
    main()
