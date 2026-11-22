"Core Basics example: JSON files (1)"

def main():
    import json
    with open("prefs.json", "w", encoding="utf-8") as f:
        json.dump({"dark": False}, f)
    with open("prefs.json", encoding="utf-8") as f:
        print(json.load(f)["dark"])


if __name__ == "__main__":
    main()
