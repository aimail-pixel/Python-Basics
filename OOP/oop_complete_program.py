"Core Basics complete program: Object-Oriented Programming (OOP)"

def main():
    class Summary:
        def label(self):
            return "Shelf"

    class Shelf(Summary):
        unit = "books"
        def __init__(self, titles):
            self._titles = list(titles)
        @property
        def titles(self):
            return tuple(self._titles)
        @classmethod
        def single(cls, title):
            return cls([title])
        @staticmethod
        def clean(title):
            return title.strip().title()
        def label(self):
            return super().label() + " of " + self.unit
        def __len__(self):
            return len(self._titles)
        def __str__(self):
            return ", ".join(self._titles)
        def __repr__(self):
            return f"Shelf({self._titles!r})"
        def __add__(self, other):
            if not isinstance(other, Shelf):
                return NotImplemented
            return Shelf(self.titles + other.titles)

    def describe(item):
        print(item.label())  # Any object supplying label() can participate.

    shelf = Shelf.single(Shelf.clean(" python ")) + Shelf(["Loops"])
    describe(Summary())
    describe(shelf)
    print(shelf, repr(shelf), len(shelf), shelf.titles)
    print([cls.__name__ for cls in Shelf.__mro__])


if __name__ == "__main__":
    main()
