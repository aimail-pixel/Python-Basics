"Core Basics example: Initialization & self (1)"

def main():
    class Lamp:
        def __init__(self, room):
            self.room = room
    print(Lamp("Study").room)


if __name__ == "__main__":
    main()
