"Core Basics example: Polymorphism & duck typing (2)"

def main():
    class Drum:
        def sound(self): return "Boom"
    class Bell:
        def sound(self): return "Ding"
    for instrument in (Drum(), Bell()):
        print(instrument.sound())


if __name__ == "__main__":
    main()
