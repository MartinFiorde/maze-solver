from src.models.window import Window
from src.models.maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(win, 50, 50, 10, 14, 50, 50)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
