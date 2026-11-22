"Core Basics example: Instance, class & static methods (2)"

def main():
    class Temperature:
        @staticmethod
        def fahrenheit(c):
            return c * 9 / 5 + 32
    print(Temperature.fahrenheit(20))


if __name__ == "__main__":
    main()
