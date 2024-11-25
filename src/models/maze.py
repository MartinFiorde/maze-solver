import time

from src.models.window import Window
from src.models.cell import Cell


class Maze:
    def __init__(
        self, win: Window, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y
    ):
        self.win = win
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = None
        self._create_cells()

    def _create_cells(self):
        self._cells = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win == None: return
        cell = Cell(
                        self.win,
                        (i + 1) * self.cell_size_x,
                        (j + 1) * self.cell_size_y,
                        (i + 2) * self.cell_size_x,
                        (j + 2) * self.cell_size_y,
                    )
        self._cells[i][j] = cell
        cell.draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.02)
