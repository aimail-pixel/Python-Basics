"Core Basics example: Arbitrary arguments (1)"

def main():
    def total(*values):
        return sum(values)
    print(total(), total(2, 3, 4))


if __name__ == "__main__":
    main()
