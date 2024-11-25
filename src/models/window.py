from tkinter import Tk, BOTH, Canvas
from src.models.line import Line


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_collor="black"):
        line.draw(self.canvas, fill_collor)
