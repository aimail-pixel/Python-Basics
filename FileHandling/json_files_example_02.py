"Core Basics example: JSON files (2)"

def main():
    import json
    s = json.dumps({"items": (2, 4)})
    print(s, type(json.loads(s)["items"]).__name__)


if __name__ == "__main__":
    main()
