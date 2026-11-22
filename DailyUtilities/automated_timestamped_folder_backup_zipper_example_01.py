"Core Basics example: Automated Timestamped Folder Backup Zipper (1)"

def main():
    import argparse
    from datetime import datetime
    from pathlib import Path
    from tempfile import NamedTemporaryFile
    from zipfile import ZipFile, ZIP_DEFLATED

    p = argparse.ArgumentParser()
    p.add_argument("source", type=Path)
    p.add_argument("destination", type=Path)
    p.add_argument("--list", action="store_true")
    a = p.parse_args()
    src, dst = a.source.resolve(), a.destination.resolve()
    if not src.is_dir() or not dst.is_dir() or dst.is_relative_to(src):
        p.error("Choose existing directories and keep the destination outside the source")
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    target = dst / f"{src.name}_{stamp}.zip"
    count = 0
    # Stage the archive first. Publish only after the ZIP writer closes.
    with NamedTemporaryFile(dir=dst, suffix=".tmp", delete=False) as temp:
        partial = Path(temp.name)
    try:
        with ZipFile(partial, "w", ZIP_DEFLATED) as z:
            for path in sorted(src.rglob("*")):
                if path.is_symlink() or not (path.is_dir() or path.is_file()):
                    continue
                name = path.relative_to(src).as_posix()
                z.write(path, name)
                count += int(path.is_file())
                if a.list:
                    print(name)
        target.hardlink_to(partial)
        print(f"Archived {count} files to {target.name}")
    finally:
        partial.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
