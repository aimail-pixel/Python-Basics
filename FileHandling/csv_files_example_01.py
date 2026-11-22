"Core Basics example: CSV files (1)"

def main():
    import csv
    with open("marks.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows([["name", "mark"], ["Roy, A", 8]])
    with open("marks.csv", newline="", encoding="utf-8") as f:
        print(next(csv.DictReader(f)))


if __name__ == "__main__":
    main()
