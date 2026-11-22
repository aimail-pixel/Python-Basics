"Core Basics example: Batch File Renamer with Prefix & Date (1)"

def main():
    import argparse
    import re
    from datetime import date
    from pathlib import Path

    p = argparse.ArgumentParser()
    p.add_argument("folder", type=Path)
    p.add_argument("prefix")
    p.add_argument("--date", type=date.fromisoformat, default=date.today())
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    if not args.folder.is_dir() or not re.fullmatch(r"[A-Za-z0-9_-]+", args.prefix):
        p.error("Use an existing folder and a prefix of letters, digits, underscores or dashes")
    stem = f"{args.prefix}_{args.date}_"
    # Reserve names from earlier runs and ignore links and hidden files.
    files = [f for f in sorted(args.folder.iterdir()) if f.is_file()
             and not f.is_symlink() and not f.name.startswith((".", stem))
             and f.resolve() != Path(__file__).resolve()]
    plan = [(f, f.with_name(f"{stem}{i:03d}{f.suffix}"))
            for i, f in enumerate(files, 1)]
    if any(dst.exists() or dst.is_symlink() for _, dst in plan):
        p.error("A target name already exists. Choose another prefix.")
    for src, dst in plan:
        if args.apply:
            src.rename(dst)
        print("RENAMED" if args.apply else "PLAN", src.name, "->", dst.name)


if __name__ == "__main__":
    main()
