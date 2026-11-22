"Core Basics complete program: Variables, Data Types & Literals"

def main():
    from decimal import Decimal
    import math

    item = "tea"
    price = Decimal("12.50")
    quantity_text = input()  # Sample input: 12
    quantity = int(quantity_text)
    available = 0 < quantity <= 0b10000
    basket = [item, quantity]
    bill = {"item": item, "total": price * quantity}
    previous = basket
    print("Order:", basket, "same basket:", previous is basket)
    print("Available:", available, "total:", bill["total"])
    print("Types:", type(price).__name__, type(available).__name__)
    print("Float check:", math.isclose(0.1 + 0.2, 0.3))


if __name__ == "__main__":
    main()
