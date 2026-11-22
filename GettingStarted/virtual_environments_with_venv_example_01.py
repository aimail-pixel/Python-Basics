"Core Basics example: Virtual environments with venv (1)"

def main():
    import sys
    print("Virtual environment" if sys.prefix != sys.base_prefix else "Base environment")


if __name__ == "__main__":
    main()
