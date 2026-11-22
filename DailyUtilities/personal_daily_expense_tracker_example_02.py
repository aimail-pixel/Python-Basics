"Core Basics example: Personal Daily Expense Tracker (2)"

def main():
    import subprocess
    import sys
    from pathlib import Path
    from tempfile import TemporaryDirectory

    # Save the utility beside this demonstration before running it.
    tool = Path(__file__).with_name("expense.py").resolve()
    with TemporaryDirectory() as folder:
        for amount, item in [("15.50", "tea"), ("30", "lunch")]:
            subprocess.run([sys.executable, tool, "add", amount, item],
                           cwd=folder, check=True)
        subprocess.run([sys.executable, tool, "total"], cwd=folder, check=True)


if __name__ == "__main__":
    main()
