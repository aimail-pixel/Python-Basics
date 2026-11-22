"Core Basics example: Nested dictionaries (2)"

def main():
    data = {"A": {"math": 90}}
    data["A"]["art"] = 75
    print(data.get("B", {}).get("art", 0))


if __name__ == "__main__":
    main()
