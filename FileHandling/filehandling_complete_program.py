"Core Basics complete program: File Handling"

def main():
    import csv
    import json
    from pathlib import Path
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as folder:
        base = Path(folder)
        table = base / "marks.csv"
        with table.open("x", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([["name", "mark"], ["Mira", 84]])
        with table.open("a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["Roy", 78])
        with table.open("r", newline="", encoding="utf-8") as f:
            print("Header:", f.readline().strip())
            print("Data rows:", len(f.readlines()))
            f.seek(0)
            scores = {r["name"]: int(r["mark"]) for r in csv.DictReader(f)}
        report = base / "report.json"
        with report.open("w", encoding="utf-8") as f:
            json.dump(scores, f, indent=2)
        with report.open(encoding="utf-8") as f:
            print("Report:", json.load(f))
        print("Closed:", f.closed)
        print("Report characters:", len(report.read_text(encoding="utf-8")))


if __name__ == "__main__":
    main()
