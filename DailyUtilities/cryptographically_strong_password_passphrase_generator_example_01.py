"Core Basics example: Cryptographically Strong Password & Passphrase Generator (1)"

def main():
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


if __name__ == "__main__":
    main()
