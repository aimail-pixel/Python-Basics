"Core Basics example: Personal Daily Expense Tracker (1)"

def main():
    import argparse
    import csv
    from datetime import date
    from decimal import Decimal, InvalidOperation
    from pathlib import Path

    p = argparse.ArgumentParser()
    commands = p.add_subparsers(dest="action", required=True)
    add = commands.add_parser("add")
    add.add_argument("amount")
    add.add_argument("note")
    commands.add_parser("total")
    args = p.parse_args()
    path = Path("expenses.csv")
    if args.action == "add":
        try:
            n = Decimal(args.amount)
            if not n.is_finite() or n <= 0 or n != n.quantize(Decimal(".01")):
                raise ValueError
        except (InvalidOperation, ValueError):
            p.error("Enter a positive amount with at most two decimal places")
        new = not path.exists() or path.stat().st_size == 0
        with path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if new:
                writer.writerow(["date", "amount", "note"])
            writer.writerow([date.today(), f"{n:.2f}", args.note])
        print(f"Recorded ₹{n:.2f}")
    else:
        total = Decimal(0)
        if path.exists():
            with path.open(newline="", encoding="utf-8") as f:
                total = sum((Decimal(r["amount"]) for r in csv.DictReader(f)), total)
        print(f"Total ₹{total:.2f}")


if __name__ == "__main__":
    main()
