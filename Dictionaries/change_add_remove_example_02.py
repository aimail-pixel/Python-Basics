"Core Basics example: Change, add & remove (2)"

def main():
    d = {"a": 1, "b": 2}
    print(d.pop("a"))
    del d["b"]
    print(d)


if __name__ == "__main__":
    main()
