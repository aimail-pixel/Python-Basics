"Core Basics example: Smart Contact & Email Extractor (2)"

def main():
    import subprocess
    import sys
    from pathlib import Path
    from tempfile import TemporaryDirectory

    # Save the utility beside this demonstration before running it.
    tool = Path(__file__).with_name("extract.py").resolve()
    with TemporaryDirectory() as folder:
        contacts = Path(folder) / "contacts.txt"
        contacts.write_text("Call +91 98765 43210 or mail ada@example.org",
                            encoding="utf-8")
        subprocess.run([sys.executable, tool, contacts, "--only", "phone"], check=True)


if __name__ == "__main__":
    main()
