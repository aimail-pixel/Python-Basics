"Core Basics example: Reading methods (1)"

def main():
    from pathlib import Path
    p = Path("lines.txt")
    p.write_text("one\ntwo\n", encoding="utf-8")
    with p.open(encoding="utf-8") as f:
        print(f.readline().rstrip(), f.read().rstrip())


if __name__ == "__main__":
    main()
