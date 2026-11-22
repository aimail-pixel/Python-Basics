"Core Basics example: Smart Contact & Email Extractor (1)"

def main():
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


if __name__ == "__main__":
    main()
