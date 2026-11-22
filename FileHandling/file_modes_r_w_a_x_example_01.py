"Core Basics example: File modes r, w, a & x (1)"

def main():
    with open("practice.txt", "w", encoding="utf-8") as f:
        f.write("Hello")
    with open("practice.txt", "r", encoding="utf-8") as f:
        print(f.read())


if __name__ == "__main__":
    main()
