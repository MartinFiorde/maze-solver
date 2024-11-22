from tkinter import Tk, BOTH, Canvas

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def draw(self, canvas: Canvas, fill_collor):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_collor, width=2)
        
    def wait_for_close(self):
        if self.running:
            self.redraw()
            
    def close(self):
        self.running = False