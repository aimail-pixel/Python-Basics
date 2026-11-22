"Core Basics example: match-case (1)"

def main():
    command = "save"
    match command:
        case "save" | "write":
            print("Saving")
        case _:
            print("Unknown")


if __name__ == "__main__":
    main()
