"Core Basics example: Instance vs class attributes (1)"

def main():
    class Course:
        language = "Python"
    a, b = Course(), Course()
    a.language = "C"
    print(a.language, b.language)


if __name__ == "__main__":
    main()
