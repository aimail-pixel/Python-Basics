"Core Basics example: Automated Timestamped Folder Backup Zipper (2)"

def main():
    import subprocess
    import sys
    from pathlib import Path
    from tempfile import TemporaryDirectory

    # Save the utility beside this demonstration before running it.
    tool = Path(__file__).with_name("backup.py").resolve()
    from zipfile import ZipFile

    with TemporaryDirectory() as folder:
        base = Path(folder)
        source = base / "notes"
        source.mkdir()
        (source / "a.txt").write_text("Study", encoding="utf-8")
        subprocess.run([sys.executable, tool, source, base], check=True,
                       capture_output=True)
        with ZipFile(next(base.glob("*.zip"))) as archive:
            print(archive.namelist(), archive.read("a.txt").decode("utf-8"))


if __name__ == "__main__":
    main()
