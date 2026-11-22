"Core Basics example: Virtual environments with venv (2)"

def main():
    import venv
    builder = venv.EnvBuilder(with_pip=True)
    print("Install pip:", builder.with_pip)


if __name__ == "__main__":
    main()
