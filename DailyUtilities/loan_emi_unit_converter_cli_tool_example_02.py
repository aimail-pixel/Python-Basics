"Core Basics example: Loan EMI & Unit Converter CLI Tool (2)"

def main():
    import subprocess
    import sys
    from pathlib import Path

    # Save the utility beside this demonstration before running it.
    tool = Path(__file__).with_name("convert.py").resolve()
    subprocess.run([sys.executable, tool, "emi", "100000", "12", "12"], check=True)
    subprocess.run([sys.executable, tool, "km", "10"], check=True)


if __name__ == "__main__":
    main()
