"Core Basics complete program: Functions, Scope & Modules"

def main():
    from statistics import mean

    SCHOOL = "Halder Academy"

    def make_report(title: str):
        calls = 0
        def report(first, /, *others, scale=1, **labels):
            nonlocal calls
            calls += 1
            scores = (first, *others)
            result = mean(scores) * scale
            return f"{SCHOOL} | {title} {calls} | {labels.get('group', 'All')} {result:g}"
        return report

    def show(message, prefix="Report"):
        print(prefix, message)

    grades = sorted([60, 90, 75], key=lambda score: -score)
    options = {"scale": 1, "group": "A"}
    run = make_report("Mean")
    show(run(*grades, **options), prefix="Class")
    show(run(80))


if __name__ == "__main__":
    main()
