"Core Basics example: Duplicate File Finder (2)"

def main():
    import subprocess
    import sys
    from pathlib import Path
    from tempfile import TemporaryDirectory

    # Save the utility beside this demonstration before running it.
    tool = Path(__file__).with_name("duplicates.py").resolve()
    with TemporaryDirectory() as folder:
        for name in ["a.txt", "b.txt"]:
            (Path(folder) / name).write_text("same", encoding="utf-8")
        subprocess.run([sys.executable, tool, folder], check=True)


if __name__ == "__main__":
    main()
