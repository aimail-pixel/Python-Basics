"Core Basics example: Packing & unpacking (2)"

def main():
    def bill(qty, rate):
        return qty * rate
    order = {"qty": 3, "rate": 12}
    print(bill(**order))


if __name__ == "__main__":
    main()
