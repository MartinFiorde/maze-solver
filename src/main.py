from src.models.window import Window
from src.models.line import Line
from src.models.point import Point
from src.models.cell import Cell


def main():
    print("hello word")
    win = Window(800, 600)
    win.draw_line(Line(Point(2, 2), Point(2, 598)), "black")
    win.draw_line(Line(Point(2, 2), Point(798, 2)), "black")
    win.draw_line(Line(Point(798, 2), Point(798, 598)), "black")
    win.draw_line(Line(Point(2, 598), Point(798, 598)), "black")
    cell1 = Cell(Point(20,20), Point(40,40), True, False, True, True)
    cell2 = Cell(Point(40,20), Point(60,40), True, True, True, False)
    win.draw_cell(cell1, "black")
    win.draw_cell(cell2, "Blue")
    cell1.draw_move(cell2)
    win.wait_for_close()


if __name__ == "__main__":
    main()
