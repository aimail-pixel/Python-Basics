"Core Basics example: Keyword arguments (1)"

def main():
    def route(start, end):
        return f"{start} → {end}"
    print(route(end="B", start="A"))


if __name__ == "__main__":
    main()
