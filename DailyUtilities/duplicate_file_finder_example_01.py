"Core Basics example: Duplicate File Finder (1)"

def main():
    import argparse
    import hashlib
    from collections import defaultdict
    from pathlib import Path

    p = argparse.ArgumentParser()
    p.add_argument("folder", type=Path)
    p.add_argument("--recursive", action="store_true")
    args = p.parse_args()
    if not args.folder.is_dir():
        p.error("Choose an existing folder")
    sizes = defaultdict(list)
    files = args.folder.rglob("*") if args.recursive else args.folder.iterdir()
    for path in sorted(files):
        if not path.is_symlink() and path.is_file():
            sizes[path.stat().st_size].append(path)
    matches = 0
    for group in sizes.values():
        if len(group) < 2:
            continue
        hashes = defaultdict(list)
        for path in group:
            digest = hashlib.sha256()
            with path.open("rb") as f:
                # Bound memory even for large files.
                for block in iter(lambda: f.read(1024 * 1024), b""):
                    digest.update(block)
            hashes[digest.hexdigest()].append(path)
        for same in hashes.values():
            if len(same) > 1:
                print("Match:", " = ".join(str(f.relative_to(args.folder)) for f in same))
                matches += 1
    if not matches:
        print("No duplicates found")


if __name__ == "__main__":
    main()
