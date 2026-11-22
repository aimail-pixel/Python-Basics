"Core Basics complete program: Daily-Life Utility Scripts"

"""Classroom toolbox. Run without arguments to see available commands.
Example: python classroom_tools.py convert km 10
Use python classroom_tools.py COMMAND --help for individual options.
"""
import sys


def run_organize():
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

def run_generate():
    import argparse
    import secrets
    import string
    from pathlib import Path

    parser = argparse.ArgumentParser(description="Generate a password or six-word phrase")
    parser.add_argument("--words", type=Path, help="UTF-8 word list, one word per line")
    args = parser.parse_args()
    if args.words:
        # Deduplicate so repeated entries cannot bias the distribution.
        words = {line.strip().casefold() for line in args.words.read_text(
            encoding="utf-8").splitlines() if line.strip().isalpha()}
        if len(words) < 2048:
            parser.error("Supply at least 2048 distinct alphabetic words")
        pool = sorted(words)
        print("-".join(secrets.choice(pool) for _ in range(6)))
    else:
        alphabet = string.ascii_letters + string.digits + "!@#$%*-_"
        print("".join(secrets.choice(alphabet) for _ in range(20)))

def run_rename_batch():
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

def run_expense():
    import argparse
    import csv
    from datetime import date
    from decimal import Decimal, InvalidOperation
    from pathlib import Path

    p = argparse.ArgumentParser()
    commands = p.add_subparsers(dest="action", required=True)
    add = commands.add_parser("add")
    add.add_argument("amount")
    add.add_argument("note")
    commands.add_parser("total")
    args = p.parse_args()
    path = Path("expenses.csv")
    if args.action == "add":
        try:
            n = Decimal(args.amount)
            if not n.is_finite() or n <= 0 or n != n.quantize(Decimal(".01")):
                raise ValueError
        except (InvalidOperation, ValueError):
            p.error("Enter a positive amount with at most two decimal places")
        new = not path.exists() or path.stat().st_size == 0
        with path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if new:
                writer.writerow(["date", "amount", "note"])
            writer.writerow([date.today(), f"{n:.2f}", args.note])
        print(f"Recorded ₹{n:.2f}")
    else:
        total = Decimal(0)
        if path.exists():
            with path.open(newline="", encoding="utf-8") as f:
                total = sum((Decimal(r["amount"]) for r in csv.DictReader(f)), total)
        print(f"Total ₹{total:.2f}")

def run_clean_notes():
    import argparse
    from pathlib import Path

    p = argparse.ArgumentParser()
    p.add_argument("source", type=Path)
    p.add_argument("--out", type=Path)
    args = p.parse_args()
    seen = set()
    lines = []
    for raw in args.source.read_text(encoding="utf-8").splitlines():
        # Split with no explicit separator to absorb tabs and repeated spaces.
        line = " ".join(raw.split())
        if line and line not in seen:
            seen.add(line)
            lines.append(line)
    if args.out:
        with args.out.open("x", encoding="utf-8") as f:
            for line in lines:
                print(line, file=f)
        print("Saved", len(lines), "lines")
    else:
        for line in lines:
            print(line)

def run_focus():
    import argparse
    import math
    import time

    def countdown(label, seconds):
        # A monotonic deadline keeps small sleep delays from accumulating.
        deadline = time.monotonic() + seconds
        while (left := math.ceil(deadline - time.monotonic())) > 0:
            print(f"\r{label} {left // 60:02d}:{left % 60:02d}", end="", flush=True)
            time.sleep(min(1, max(0, deadline - time.monotonic())))
        print("\a")

    p = argparse.ArgumentParser()
    p.add_argument("--seconds", type=int, default=1500)
    p.add_argument("--rest", type=int, default=300)
    args = p.parse_args()
    if min(args.seconds, args.rest) < 1:
        p.error("Durations must be positive")
    try:
        countdown("Focus", args.seconds)
        countdown("Break", args.rest)
        print("Session complete")
    except KeyboardInterrupt:
        print("\nSession stopped")

def run_duplicates():
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

def run_convert():
    import argparse
    import math

    p = argparse.ArgumentParser()
    cmd = p.add_subparsers(dest="kind", required=True)
    emi = cmd.add_parser("emi")
    emi.add_argument("principal", type=float)
    emi.add_argument("rate", type=float)
    emi.add_argument("months", type=int)
    km = cmd.add_parser("km")
    km.add_argument("distance", type=float)
    a = p.parse_args()
    if a.kind == "km":
        if not math.isfinite(a.distance) or a.distance < 0:
            p.error("Distance must be finite and nonnegative")
        print(f"{a.distance / 1.609344:.3f} miles")
    else:
        if (not all(map(math.isfinite, (a.principal, a.rate)))
                or a.principal <= 0 or a.rate < 0 or a.months < 1):
            p.error("Use positive principal and months, and a nonnegative rate")
        r = a.rate / 1200
        # expm1 and log1p avoid cancellation at small positive interest rates.
        payment = (a.principal / a.months if r == 0 else
                   a.principal * r / -math.expm1(-a.months * math.log1p(r)))
        print(f"Monthly EMI ₹{payment:.2f}")

def run_extract():
    import argparse
    import re
    from pathlib import Path

    p = argparse.ArgumentParser()
    p.add_argument("source", type=Path)
    p.add_argument("--only", choices=["email", "phone"])
    args = p.parse_args()
    text = args.source.read_text(encoding="utf-8")
    email = r"[\w.+-]+@(?:[\w-]+\.)+[a-zA-Z]{2,}"
    phone = r"(?<![+\d])(?:\+91[ -]?)?([6-9]\d{4})[ -]?(\d{5})(?!\d)"
    if args.only != "phone":
        # Keep first-seen order while removing repeats.
        for value in dict.fromkeys(re.findall(email, text, re.ASCII)):
            print("Email:", value)
    if args.only != "email":
        numbers = ["+91" + a + b for a, b in re.findall(phone, text, re.ASCII)]
        for value in dict.fromkeys(numbers):
            print("Phone:", value)

def run_backup():
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

COMMANDS = {
    "organize": run_organize,
    "generate": run_generate,
    "rename_batch": run_rename_batch,
    "expense": run_expense,
    "clean_notes": run_clean_notes,
    "focus": run_focus,
    "duplicates": run_duplicates,
    "convert": run_convert,
    "extract": run_extract,
    "backup": run_backup,
}

def main():
    if len(sys.argv) == 1:
        print("Available commands:", ", ".join(COMMANDS))
        return
    name = sys.argv.pop(1)
    if name not in COMMANDS:
        raise SystemExit("Unknown command: " + name)
    COMMANDS[name]()

if __name__ == "__main__":
    main()
