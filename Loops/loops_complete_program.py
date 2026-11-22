"Core Basics complete program: Loops & Iteration"

def main():
    requests = [0, 4, 9]
    while requests:
        wanted = requests.pop(0)
        if wanted == 0:
            continue
        for row in range(2):
            for col in range(1, 4):
                seat = row * 3 + col
                if seat == wanted:
                    print("Found", wanted, "row", row + 1, "column", col)
                    break
            else:
                # This row was exhausted, so inspect the next row.
                continue
            break
        else:
            print("Missing", wanted)
        if wanted == 4:
            pass  # A reserved seat needs no additional action here.


if __name__ == "__main__":
    main()
