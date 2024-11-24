from src.models.window import Window
from src.models.line import Line
from src.models.point import Point
from src.models.cell import Cell


def main():
    print("hello word")
    win = Window(800, 600)
    cell1 = Cell(win, 20, 20, 40, 40, rw=False, bw=False)
    cell2 = Cell(win, 40, 20, 60, 40, lw=False)
    cell3 = Cell(win, 20, 40, 40, 60, tw=False, bw=False)
    cell4 = Cell(win, 20, 60, 40, 80, tw=False)
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    cell2.draw_move(cell1)
    cell1.draw_move(cell3)
    cell3.draw_move(cell4)
    win.wait_for_close()


if __name__ == "__main__":
    main()
