"Core Basics example: assert (2)"

def main():
    try:
        assert 3 < 2, "Unexpected ordering"
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
