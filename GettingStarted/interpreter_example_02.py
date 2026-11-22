"Core Basics example: Interpreter (2)"

def main():
    import ast
    tree = ast.parse("total = 42")
    print(type(tree.body[0]).__name__)


if __name__ == "__main__":
    main()
