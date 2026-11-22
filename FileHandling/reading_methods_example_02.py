"Core Basics example: Reading methods (2)"

def main():
    from io import StringIO
    with StringIO("A\nB\n") as f:
        print([line.rstrip() for line in f])
        f.seek(0)
        print(f.readlines())


if __name__ == "__main__":
    main()
