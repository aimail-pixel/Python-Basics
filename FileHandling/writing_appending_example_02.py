"Core Basics example: Writing & appending (2)"

def main():
    from pathlib import Path
    p = Path("journal.txt")
    p.write_text("Start\n", encoding="utf-8")
    with p.open("a", encoding="utf-8") as f:
        print("Finish", file=f)
    print(p.read_text(encoding="utf-8").rstrip())


if __name__ == "__main__":
    main()
