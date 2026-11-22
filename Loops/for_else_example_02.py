"Core Basics example: for-else (2)"

def main():
    for word in ["pen", "book"]:
        if word == "book":
            print("Found")
            break
    else:
        print("Missing")


if __name__ == "__main__":
    main()
