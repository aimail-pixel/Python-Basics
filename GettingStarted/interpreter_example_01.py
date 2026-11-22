"Core Basics example: Interpreter (1)"

def main():
    program = compile("6 * 7", "<lesson>", "eval")
    print(eval(program))


if __name__ == "__main__":
    main()
