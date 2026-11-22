"Core Basics example: Smart Downloads Folder Organizer (2)"

def main():
    import subprocess
    import sys
    from pathlib import Path
    from tempfile import TemporaryDirectory

    # Save the utility beside this demonstration before running it.
    tool = Path(__file__).with_name("organize.py").resolve()
    with TemporaryDirectory() as folder:
        target = Path(folder)
        (target / "notes.pdf").touch()
        subprocess.run([sys.executable, tool, folder, "--apply"], check=True)
        print("Moved:", (target / "Documents" / "notes.pdf").exists())


if __name__ == "__main__":
    main()
