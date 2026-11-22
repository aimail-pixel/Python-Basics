"Core Basics example: Syntax vs runtime errors (1)"

def main():
    try:
        compile("if True print(3)", "lesson.py", "exec")
    except SyntaxError:
        print("Invalid syntax")


if __name__ == "__main__":
    main()
