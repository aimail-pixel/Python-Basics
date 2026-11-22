"Core Basics example: Conditional user inputs (1)"

def main():
    reply = input().strip().lower()
    print("Confirmed" if reply in ("yes", "y") else "Pending")


if __name__ == "__main__":
    main()
