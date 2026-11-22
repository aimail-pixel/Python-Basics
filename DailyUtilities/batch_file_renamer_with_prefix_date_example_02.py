"Core Basics example: Batch File Renamer with Prefix & Date (2)"

def main():
    import subprocess
    import sys
    from pathlib import Path
    from tempfile import TemporaryDirectory

    # Save the utility beside this demonstration before running it.
    tool = Path(__file__).with_name("rename_batch.py").resolve()
    with TemporaryDirectory() as folder:
        (Path(folder) / "sky.jpg").touch()
        subprocess.run([sys.executable, tool, folder, "trip", "--date",
                        "2026-03-10", "--apply"], check=True)
        print(sorted(p.name for p in Path(folder).iterdir()))


if __name__ == "__main__":
    main()
