"Core Basics example: Typecodes i, f and d (2)"

def main():
    from array import array
    for code in "fd":
        print(f"{array(code, [0.1])[0]:.10f}")


if __name__ == "__main__":
    main()
