"Core Basics example: Function annotations (2)"

def main():
    from typing import get_type_hints
    def title(name: str) -> str:
        return name.title()
    print(get_type_hints(title)["return"].__name__)


if __name__ == "__main__":
    main()
