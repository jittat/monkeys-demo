import tkinter as tk
import tkinter.ttk as ttk
 
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY = 33

class Sprite():
    def __init__(self, canvas, image_filename, x=0, y=0):
        self.image_filename = image_filename
        self.x = x
        self.y = y
        self.canvas = canvas

        self.init_canvas_object()    

    def init_canvas_object(self):
        self.photo_image = tk.PhotoImage(file=self.image_filename)
        self.canvas_object_id = self.canvas.create_image(
            self.x, 
            self.y,
            image=self.photo_image)

    def render(self):
        self.canvas.coords(self.canvas_object_id, self.x, self.y)

    def update(self):
        pass

class Banana(Sprite):
    def update(self):
        self.x += 5

class MonkeyGame(ttk.Frame):
 
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(sticky="news")
        self.create_widgets()

        self.create_sprites()
 
    def create_widgets(self):
        self.canvas = tk.Canvas(self, borderwidth=0,
            width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0)
        self.canvas.grid(sticky="news")

    def create_sprites(self):
        self.banana = Banana(self.canvas, 'banana.png', 100, 100)

    def animate(self):
        self.banana.update()
        self.banana.render()

        self.after(UPDATE_DELAY, self.animate)

    def start(self):
        self.after(0, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Game")
 
    # do not allow window resizing
    root.resizable(False, False)
    app = MonkeyGame(root)
    app.start()
    root.mainloop()
