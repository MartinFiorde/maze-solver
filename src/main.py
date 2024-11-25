from src.models.window import Window
from src.models.maze import Maze


def main():
    print("hello word")
    win = Window(800, 600)
    maze = Maze(win, 50, 50, 14, 10, 50, 50)
    win.wait_for_close()


if __name__ == "__main__":
    main()
