"Core Basics example: Arbitrary arguments (2)"

def main():
    def fields(**kwargs):
        for k, v in kwargs.items():
            print(k, v)
    fields(city="Pune", seats=3)


if __name__ == "__main__":
    main()
