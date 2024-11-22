from src.models.window import Window
from src.models.line import Line
from src.models.point import Point


def main():
    print("hello word")
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 20), Point(30, 40)), "red")
    win.draw_line(Line(Point(2, 2), Point(2, 598)), "black")
    win.draw_line(Line(Point(2, 2), Point(798, 2)), "black")
    win.draw_line(Line(Point(798, 2), Point(798, 598)), "black")
    win.draw_line(Line(Point(2, 598), Point(798, 598)), "black")
    win.draw_line(Line(Point(10, 40), Point(20, 30)), "blue")
    win.wait_for_close()


if __name__ == "__main__":
    main()
