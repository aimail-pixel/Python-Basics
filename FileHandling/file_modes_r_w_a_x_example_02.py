"Core Basics example: File modes r, w, a & x (2)"

def main():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    with TemporaryDirectory() as folder:
        p = Path(folder) / "new.txt"
        with p.open("x") as f:
            f.write("A")
        with p.open("a") as f:
            f.write("B")
        print(p.read_text())


if __name__ == "__main__":
    main()
