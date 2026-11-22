"Core Basics example: Tuple update workaround (1)"

def main():
    a = (10, 20, 30)
    b = a[:1] + (99,) + a[2:]
    print(a, b)


if __name__ == "__main__":
    main()
