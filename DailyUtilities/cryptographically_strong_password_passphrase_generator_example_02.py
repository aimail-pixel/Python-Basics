"Core Basics example: Cryptographically Strong Password & Passphrase Generator (2)"

def main():
    import subprocess
    import sys
    from pathlib import Path

    # Save the utility beside this demonstration before running it.
    tool = Path(__file__).with_name("generate.py").resolve()
    result = subprocess.run([sys.executable, tool], capture_output=True,
                            text=True, check=True)
    print("Password length:", len(result.stdout.strip()))


if __name__ == "__main__":
    main()
