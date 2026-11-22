"Core Basics example: Terminal Pomodoro Focus Timer (1)"

def main():
    import argparse
    import math
    import time

    def countdown(label, seconds):
        # A monotonic deadline keeps small sleep delays from accumulating.
        deadline = time.monotonic() + seconds
        while (left := math.ceil(deadline - time.monotonic())) > 0:
            print(f"\r{label} {left // 60:02d}:{left % 60:02d}", end="", flush=True)
            time.sleep(min(1, max(0, deadline - time.monotonic())))
        print("\a")

    p = argparse.ArgumentParser()
    p.add_argument("--seconds", type=int, default=1500)
    p.add_argument("--rest", type=int, default=300)
    args = p.parse_args()
    if min(args.seconds, args.rest) < 1:
        p.error("Durations must be positive")
    try:
        countdown("Focus", args.seconds)
        countdown("Break", args.rest)
        print("Session complete")
    except KeyboardInterrupt:
        print("\nSession stopped")


if __name__ == "__main__":
    main()
