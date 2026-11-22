"Core Basics example: else & finally (2)"

def main():
    def demo():
        try:
            return 7
        finally:
            print("Cleanup")
    print(demo())


if __name__ == "__main__":
    main()
