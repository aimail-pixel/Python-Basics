"Core Basics example: Access with get() (1)"

def main():
    d = {"count": 0}
    print(d["count"], d.get("limit", 5))


if __name__ == "__main__":
    main()
