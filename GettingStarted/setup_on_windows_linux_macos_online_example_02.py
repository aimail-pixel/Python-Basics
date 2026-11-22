"Core Basics example: Setup on Windows, Linux, macOS & online (2)"

def main():
    from pathlib import Path
    print("Working folder exists:", Path.cwd().is_dir())


if __name__ == "__main__":
    main()
