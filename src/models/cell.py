from tkinter import Tk, BOTH, Canvas

class Cell:
    def __init__(self, p1, p2, wt, wr, wb, wl):
        self.has_top_wall = wt
        self.has_right_wall = wr
        self.has_bottom_wall = wb
        self.has_left_wall = wl
        self._x1 = p1.x
        self._x2 = p2.x
        self._y1 = p1.y
        self._y2 = p2.y
        self._win = False

        
    def draw(self, canvas: Canvas, fill_color):
        if self.has_top_wall:
            canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill=fill_color, width=2)
        if self.has_right_wall:
            canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill=fill_color, width=2)
        if self.has_bottom_wall:
            canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill=fill_color, width=2)
        if self.has_left_wall:
            canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill=fill_color, width=2)
        
    def wait_for_close(self):
        if self.running:
            self.redraw()
            
    def close(self):
        self.running = False