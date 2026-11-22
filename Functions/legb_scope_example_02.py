"Core Basics example: LEGB scope (2)"

def main():
    def counter():
        n = 0
        def next_value():
            nonlocal n
            n += 1
            return n
        return next_value
    tick = counter()
    print(tick(), tick())


if __name__ == "__main__":
    main()
