"Core Basics complete program: Arrays (array module)"

def main():
    from array import array

    metadata = ["Room A", 3]  # Mixed-type list for descriptive fields
    ids = array("i", [1, 3])
    ids.insert(1, 2)
    samples = array("f", [20, 21.5])
    samples.append(23)
    samples[0] = 19.5
    samples.remove(23)
    samples.extend([24, 99])
    print("Discarded:", samples.pop())
    archive = array("d", samples)
    restored = array("d")
    restored.frombytes(archive.tobytes())
    print(metadata, "ids:", ids.tolist())
    print("First:", restored[0], "all:", restored.tolist())
    print("Packed bytes:", len(restored) * restored.itemsize)


if __name__ == "__main__":
    main()
