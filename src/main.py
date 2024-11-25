import argparse

from src.models.window import Window
from src.models.maze import Maze


def main(seed1, seed2):
    win = Window(800, 600)
    maze = Maze(win, 50, 50, 10, 14, 50, 50, seed1)
    maze.solve(seed2)
    win.wait_for_close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute the script with seeds to replicate random values")
    parser.add_argument("seed1", nargs="?", type=int, default=None, help="Seed for maze generator (optional).")
    parser.add_argument("seed2", nargs="?", type=int, default=None, help="seed for maze solver (optional).")

    args = parser.parse_args()
    main(args.seed1, args.seed2)
