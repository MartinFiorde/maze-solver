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
        self._break_entrance_and_exit()


    def _create_cells(self):
        self._cells = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = Cell(
                        self.win,
                        (i + 1) * self.cell_size_x,
                        (j + 1) * self.cell_size_y,
                        (i + 2) * self.cell_size_x,
                        (j + 2) * self.cell_size_y,
                    )
        self._cells[i][j] = cell
        if self.win != None:
            cell.draw()
            self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        entrance: Cell = self._cells[0][0]
        exit: Cell = self._cells[-1][-1]
        entrance.has_top_wall = False
        exit.has_bottom_wall = False
        if self.win != None:
            entrance.draw()
            exit.draw()
        