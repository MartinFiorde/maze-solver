from src.models.window import Window
from src.models.line import Line
from src.models.point import Point


class Maze:
    def __init__(self, win: Window, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y):
        self.win = win
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._create_cells()
        
    def _create_cells(self):
        pass
    
    def _draw_cell(self, i, j):
        pass
    
    def _animate(self):
        pass