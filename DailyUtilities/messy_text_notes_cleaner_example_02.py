"Core Basics example: Messy Text & Notes Cleaner (2)"

def main():
    import subprocess
    import sys
    from pathlib import Path
    from tempfile import TemporaryDirectory

    # Save the utility beside this demonstration before running it.
    tool = Path(__file__).with_name("clean_notes.py").resolve()
    with TemporaryDirectory() as folder:
        notes = Path(folder) / "notes.txt"
        notes.write_text(" Buy  milk\nBuy milk\nRead\tPython\n", encoding="utf-8")
        subprocess.run([sys.executable, tool, notes], check=True)


if __name__ == "__main__":
    main()
