from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self, canvas: Canvas, fill_collor):
        canvas.create_line(self.x, self.y, self.x*2, self.y*2, fill=fill_collor, width=self.x*2)
        
    def wait_for_close(self):
        if self.running:
            self.redraw()
            
    def close(self):
        self.running = False