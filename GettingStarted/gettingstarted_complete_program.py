"Core Basics complete program: Overview, Environment & Basic Program"

"""Run as a script or paste the whole program into a notebook cell."""
import sys
from pathlib import Path

def main():
    # Inspect the environment in which the lesson actually runs.
    print("Python 3.10+:", sys.version_info >= (3, 10))
    print("Environment:", "virtual" if sys.prefix != sys.base_prefix else "base")
    print("Working directory ready:", Path.cwd().is_dir())
    source = 'print("First class:", 3 * 15, "minutes")'
    program = compile(source, "<classroom>", "exec")
    print("Stage:", type(program).__name__)
    exec(program)  # Execute only the fixed lesson text above.

if __name__ == "__main__":
    main()
