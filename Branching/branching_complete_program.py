"Core Basics complete program: Control Flow & Decision Making"

def main():
    raw = input().strip()  # Sample input: 12
    try:
        age = int(raw)
    except ValueError:
        print("Enter a whole age")
    else:
        if age < 0:
            print("Invalid age")
        else:
            if age < 5:
                band = "free"
            elif age < 18:
                band = "student"
            else:
                band = "adult"
            match band:
                case "free": fare = 0
                case "student": fare = 20
                case _: fare = 50
            if fare:
                print("Payment required")
            print(band, fare)


if __name__ == "__main__":
    main()
