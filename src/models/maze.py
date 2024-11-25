import time
import random

from src.models.window import Window
from src.models.cell import Cell


class Maze:
    def __init__(
        self,
        win: Window,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        seed=None,
    ):
        self.win = win
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y

        if seed != None:
            random.seed(seed)
        self._cells: list[list[Cell]] = None
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        self._cells = [
            [None for _ in range(self.num_rows)] for _ in range(self.num_cols)
        ]
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
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
        entrance: Cell = self._cells[0][0]
        exit: Cell = self._cells[-1][-1]
        entrance.has_top_wall = False
        exit.has_bottom_wall = False
        if self.win != None:
            entrance.draw()
            exit.draw()

    def _break_walls_r(self, i, j):
        cell: Cell = self._cells[i][j]
        cell.visited = True
        while True:
            to_visit = []
            if i != 0 and not self._cells[i - 1][j].visited:
                to_visit.append((-1, 0))
            if j != 0 and not self._cells[i][j - 1].visited:
                to_visit.append((0, -1))
            if i != (self.num_cols - 1) and not self._cells[i + 1][j].visited:
                to_visit.append((1, 0))
            if j != (self.num_rows - 1) and not self._cells[i][j + 1].visited:
                to_visit.append((0, 1))
            if len(to_visit) == 0:
                if self.win != None:
                    cell.draw()
                    self._animate()
                return

            idx_random = random.randint(0, len(to_visit) - 1)
            m, n = to_visit.pop(idx_random)
            if m == -1:
                cell.has_left_wall = False
                self._cells[i + m][j + n].has_right_wall = False
            if m == 1:
                cell.has_right_wall = False
                self._cells[i + m][j + n].has_left_wall = False
            if n == -1:
                cell.has_top_wall = False
                self._cells[i + m][j + n].has_bottom_wall = False
            if n == 1:
                cell.has_bottom_wall = False
                self._cells[i + m][j + n].has_top_wall = False

            self._break_walls_r(i + m, j + n)
