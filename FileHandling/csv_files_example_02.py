"Core Basics example: CSV files (2)"

def main():
    import csv
    from io import StringIO
    rows = csv.DictReader(StringIO("qty,price\n2,15\n3,10\n"))
    print(sum(int(r["qty"]) * int(r["price"]) for r in rows))


if __name__ == "__main__":
    main()
