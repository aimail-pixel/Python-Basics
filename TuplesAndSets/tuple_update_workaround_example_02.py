"Core Basics example: Tuple update workaround (2)"

def main():
    record = ("Mira", [80])
    record[1].append(90)
    print(record)


if __name__ == "__main__":
    main()
