"Core Basics example: Loop over dictionaries (2)"

def main():
    d = {"a": 0, "b": 4}
    for key in list(d):
        if d[key] == 0:
            del d[key]
    print(d)


if __name__ == "__main__":
    main()
