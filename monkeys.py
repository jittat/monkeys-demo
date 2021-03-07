import tkinter as tk
import tkinter.ttk as ttk
 
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500
 
class MonkeyGame(ttk.Frame):
 
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(sticky="news")
        self.create_widgets()
 
    def create_widgets(self):
        self.canvas = tk.Canvas(self, borderwidth=0,
            width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0)
        self.canvas.grid(sticky="news")

 
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Game")
 
    # do not allow window resizing
    root.resizable(False, False)
    app = MonkeyGame(root)
    root.mainloop()
