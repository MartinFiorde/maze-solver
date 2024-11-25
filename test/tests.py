import unittest

from src.models.maze import Maze
from src.models.cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(None, 0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(None, 0, 0, num_rows, num_cols, 10, 10)
        entrance: Cell = maze._cells[0][0]
        exit: Cell = maze._cells[-1][-1]
        self.assertFalse(entrance.has_top_wall)
        self.assertFalse(exit.has_bottom_wall)
        
    def test_maze__reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(None, 0, 0, num_rows, num_cols, 10, 10)
        for row in maze._cells:
            for cell in row:
                self.assertFalse(cell.visited)