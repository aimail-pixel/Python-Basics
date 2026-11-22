"Core Basics complete program: Lists"

def main():
    books = ["Loops", "Files", "Python"]
    print("First:", books[0], "preview:", books[:2])
    books[1] = "Text"
    books.append("Sets")
    books.insert(1, "Lists")
    books.extend(["Text", "Draft"])
    print("Text copies:", books.count("Text"), "first at", books.index("Text"))
    books.remove("Text")
    print("Removed:", books.pop())
    saved = books.copy()
    books.sort(key=str.casefold)
    for number, title in enumerate(books, 1):
        print(number, title)
    short = [title for title in books if len(title) < 5]
    combined = short + ["OOP"]
    combined.reverse()
    print("Joined:", combined, "saved:", saved)
    books.clear()
    print("Remaining:", len(books))


if __name__ == "__main__":
    main()
