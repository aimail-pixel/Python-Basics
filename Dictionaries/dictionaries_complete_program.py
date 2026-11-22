"Core Basics complete program: Dictionaries"

def main():
    register = {"A": {"math": 71}, "B": {"math": 89}}
    register["A"]["math"] = 75
    register.setdefault("C", {}).update(math=80)
    register["D"] = {"math": 0}
    removed = register.pop("D")
    totals = {key: sum(subjects.values()) for key, subjects in register.items()}
    for name, total in totals.items():
        print(name, total)
    print("Missing:", register.get("Z", {}))
    print("Names:", list(register.keys()), "withdrawn:", removed["math"])


if __name__ == "__main__":
    main()
