"Core Basics example: Remove from sets (1)"

def main():
    s = {2, 4}
    s.discard(7)
    s.remove(2)
    print(sorted(s))


if __name__ == "__main__":
    main()
