"Core Basics example: Loop over lists (2)"

def main():
    kept = []
    for n in [2, 5, 8]:
        if n >= 5:
            kept.append(n)
    print(kept)


if __name__ == "__main__":
    main()
