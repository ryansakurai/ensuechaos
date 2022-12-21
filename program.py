import time
import random
import argparse


def infinite_loop() -> None:
    while True:
        print(random.choice(("A", "a", " ")), end="")


def timed_loop(seconds: int) -> None:
    initial_time = time.time()
    while time.time() - initial_time < seconds:
        print(random.choice(("A", "a", " ")), end="")


def main():
    parser = argparse.ArgumentParser("Spam Me")
    parser.add_argument("--time", "-t", type=int, default=5, help="Time of execution in seconds")
    parser.add_argument("--infinite", "-i", action="store_true", help="Time of execution is infinite")

    args = parser.parse_args()

    if args.infinite:
        infinite_loop()
    else:
        timed_loop(args.time)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
