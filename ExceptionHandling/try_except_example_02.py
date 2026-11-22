"Core Basics example: try & except (2)"

def main():
    try:
        print({"a": 1}["b"])
    except KeyError as err:
        print("Missing key", err.args[0])


if __name__ == "__main__":
    main()
