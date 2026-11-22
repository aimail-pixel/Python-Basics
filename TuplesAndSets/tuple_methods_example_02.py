"Core Basics example: Tuple methods (2)"

def main():
    t = ("tea", "rice")
    print(t.index("oil") if "oil" in t else "Missing")


if __name__ == "__main__":
    main()
