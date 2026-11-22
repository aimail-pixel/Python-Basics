"Core Basics example: Tuple exercises (2)"

def main():
    cities = ("A", "B", "C")
    print(tuple(zip(cities, cities[1:])))


if __name__ == "__main__":
    main()
