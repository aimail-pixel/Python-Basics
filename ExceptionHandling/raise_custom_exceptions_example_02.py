"Core Basics example: raise & custom exceptions (2)"

def main():
    class SoldOut(Exception):
        pass
    try:
        raise SoldOut("No seats left")
    except SoldOut as e:
        print(e)


if __name__ == "__main__":
    main()
