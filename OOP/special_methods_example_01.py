"Core Basics example: Special methods (1)"

def main():
    class Deck:
        def __init__(self, cards): self.cards = list(cards)
        def __len__(self): return len(self.cards)
        def __str__(self): return ", ".join(self.cards)
        def __repr__(self): return f"Deck({self.cards!r})"
    d = Deck(["A", "K"])
    print(str(d), repr(d), len(d))


if __name__ == "__main__":
    main()
