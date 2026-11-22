"Core Basics example: continue (2)"

def main():
    n = 0
    while n < 4:
        n += 1
        if n % 2:
            continue
        print(n)


if __name__ == "__main__":
    main()
