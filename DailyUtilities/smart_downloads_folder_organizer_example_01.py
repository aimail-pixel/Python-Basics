"Core Basics example: Smart Downloads Folder Organizer (1)"

def main():
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description="Group downloaded files by type")
    parser.add_argument("folder", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not args.folder.is_dir():
        parser.error("Choose an existing directory")
    groups = {"Documents": ".pdf .docx .txt", "Images": ".jpg .jpeg .png .gif",
              "Archives": ".zip .gz .tar", "Audio": ".mp3 .wav"}
    for source in sorted(args.folder.iterdir()):
        # Skip directories, symbolic links, hidden files and this script.
        if (source.is_symlink() or not source.is_file() or source.name.startswith(".")
                or source.resolve() == Path(__file__).resolve()):
            continue
        category = next((g for g, exts in groups.items()
                         if source.suffix.lower() in exts.split()), "Other")
        target = args.folder / category / source.name
        if target.parent.is_symlink() or target.exists() or target.is_symlink():
            print("SKIP", source.name)
            continue
        if args.apply:
            target.parent.mkdir(exist_ok=True)
            source.rename(target)
        print("MOVED" if args.apply else "PLAN", source.name, "->",
              target.relative_to(args.folder).as_posix())


if __name__ == "__main__":
    main()
