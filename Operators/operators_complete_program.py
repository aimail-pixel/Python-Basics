"Core Basics complete program: Operators & Expressions"

def main():
    permissions = 0b0101
    write_bit = 0b0010
    permissions |= write_bit
    users = ["Mira", "Roy"]
    roster = users
    minutes = 73
    hours, remainder = minutes // 60, minutes % 60
    print("Time:", hours, remainder, "minutes")
    print("Read enabled:", bool(permissions & 1))
    print("Toggle write:", permissions ^ write_bit)
    print("Shifts:", permissions << 1, permissions >> 1)
    if (count := len(users)) >= 2 and "Mira" in users:
        print("Included:", count, roster is users)
    print("Fee:", (hours + 1) * 10 - 2, "average:", minutes / count)
    print("Capacity:", 2 ** 3, "full:", count == 8 or not users)


if __name__ == "__main__":
    main()
