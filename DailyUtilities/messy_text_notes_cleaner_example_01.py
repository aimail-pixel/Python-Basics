"Core Basics example: Messy Text & Notes Cleaner (1)"

def main():
    import argparse
    from pathlib import Path

    p = argparse.ArgumentParser()
    p.add_argument("source", type=Path)
    p.add_argument("--out", type=Path)
    args = p.parse_args()
    seen = set()
    lines = []
    for raw in args.source.read_text(encoding="utf-8").splitlines():
        # Split with no explicit separator to absorb tabs and repeated spaces.
        line = " ".join(raw.split())
        if line and line not in seen:
            seen.add(line)
            lines.append(line)
    if args.out:
        with args.out.open("x", encoding="utf-8") as f:
            for line in lines:
                print(line, file=f)
        print("Saved", len(lines), "lines")
    else:
        for line in lines:
            print(line)


if __name__ == "__main__":
    main()
