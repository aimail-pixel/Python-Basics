"Core Basics example: Polymorphism & duck typing (1)"

def main():
    from io import StringIO
    def headline(reader):
        return reader.readline().strip()
    print(headline(StringIO("News\nMore")))


if __name__ == "__main__":
    main()
