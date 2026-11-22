"Core Basics complete program: Strings & Text Manipulation"

def main():
    raw = "  mira   roy  "
    parts = raw.strip().title().split()
    name = " ".join(parts)
    initials = "".join(part[0] for part in parts)
    badge = initials + "-" + name[:4].upper()
    print(f"Name:\t{name}")
    print(f"Badge:\t{badge}")
    print("Reverse:", initials[::-1])
    print("Updated label:", badge.replace("-", "/"))
    print("Original input:", repr(raw))


if __name__ == "__main__":
    main()
