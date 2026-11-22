"Core Basics example: Writing & appending (1)"

def main():
    with open("log.txt", "w", encoding="utf-8") as f:
        f.writelines(["one\n", "two\n"])
    with open("log.txt", encoding="utf-8") as f:
        print(f.read().rstrip())


if __name__ == "__main__":
    main()
