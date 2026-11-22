"Core Basics example: Creating arrays (2)"

def main():
    from array import array
    samples = array("d")
    samples.extend([1, 2.5])
    print(samples.tolist())


if __name__ == "__main__":
    main()
