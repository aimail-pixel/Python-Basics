"Core Basics example: Loan EMI & Unit Converter CLI Tool (1)"

def main():
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


if __name__ == "__main__":
    main()
