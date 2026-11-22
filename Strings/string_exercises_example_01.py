"Core Basics example: String exercises (1)"

def main():
    name = "  Ada   Roy "
    print("".join(w[0].upper() for w in name.split()))


if __name__ == "__main__":
    main()
