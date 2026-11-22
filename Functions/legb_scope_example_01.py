"Core Basics example: LEGB scope (1)"

def main():
    label = "global"
    def outer():
        label = "enclosing"
        def inner():
            return label
        return inner()
    print(outer())


if __name__ == "__main__":
    main()
