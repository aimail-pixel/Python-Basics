"Core Basics example: Encapsulation & property (2)"

def main():
    class Score:
        @property
        def value(self):
            return self._value
        @value.setter
        def value(self, n):
            if not 0 <= n <= 100:
                raise ValueError("Score outside 0–100")
            self._value = n
    s = Score()
    s.value = 80
    print(s.value)


if __name__ == "__main__":
    main()
