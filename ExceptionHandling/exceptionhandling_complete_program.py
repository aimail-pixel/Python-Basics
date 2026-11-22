"Core Basics complete program: Errors & Exception Handling"

def main():
    class InvalidMark(ValueError):
        """A numeric mark outside the allowed range."""

    def check(raw):
        n = int(raw)
        if not 0 <= n <= 100:
            raise InvalidMark("out of range")
        return n

    try:
        compile("if True print(0)", "sample.py", "exec")
    except SyntaxError:
        print("Syntax check failed")

    accepted = []
    for raw in ("80", "x", "105", None):
        try:
            mark = check(raw)
        except InvalidMark as error:
            print("Rejected:", error)
        except (ValueError, TypeError):
            print("Unreadable:", raw)
        else:
            accepted.append(mark)
        finally:
            print("Record processed")
    assert all(0 <= n <= 100 for n in accepted)
    print("Accepted:", accepted)


if __name__ == "__main__":
    main()
