"Core Basics example: Terminal Pomodoro Focus Timer (2)"

def main():
    import subprocess
    import sys
    from pathlib import Path

    # Save the utility beside this demonstration before running it.
    tool = Path(__file__).with_name("focus.py").resolve()
    # Two short stages demonstrate the full session in two seconds.
    subprocess.run([sys.executable, tool, "--seconds", "1", "--rest", "1"], check=True)


if __name__ == "__main__":
    main()
