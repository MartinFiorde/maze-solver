from tkinter import Tk, BOTH, Canvas
from src.models.line import Line
from src.models.cell import Cell


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = True
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_collor):
        line.draw(self.canvas, fill_collor)

    def draw_cell(self, cell: Cell, fill_collor):
        cell.draw(self.canvas, fill_collor)
