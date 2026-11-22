"Core Basics example: Join sets (2)"

def main():
    a = {1, 2}
    a.update({2, 3})
    print(sorted(a))


if __name__ == "__main__":
    main()
