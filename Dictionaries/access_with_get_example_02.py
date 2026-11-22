"Core Basics example: Access with get() (2)"

def main():
    d = {"note": None}
    print(d.get("note"), "note" in d, "other" in d)


if __name__ == "__main__":
    main()
