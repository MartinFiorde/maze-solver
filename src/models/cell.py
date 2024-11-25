from src.models.window import Window
from src.models.line import Line
from src.models.point import Point


class Cell:
    def __init__(self, win: Window, x1, y1, x2, y2, tw=True, rw=True, bw=True, lw=True):
        self._win = win
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.has_top_wall = tw
        self.has_right_wall = rw
        self.has_bottom_wall = bw
        self.has_left_wall = lw

    def draw(self):
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            )
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            )
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            )
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            )

    def draw_move(self, to_cell: "Cell", undo=False):
        fill_color = "gray" if undo else "red"
        x1 = (self._x1 + self._x2) / 2
        y1 = (self._y1 + self._y2) / 2
        x2 = (to_cell._x1 + to_cell._x2) / 2
        y2 = (to_cell._y1 + to_cell._y2) / 2

        self._win.draw_line(Line(Point(x1, y1), Point(x2, y2)), fill_color)
