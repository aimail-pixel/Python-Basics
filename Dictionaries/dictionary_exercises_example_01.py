"Core Basics example: Dictionary exercises (1)"

def main():
    counts = {}
    for word in "tea rice tea".split():
        counts[word] = counts.get(word, 0) + 1
    print(counts)


if __name__ == "__main__":
    main()
