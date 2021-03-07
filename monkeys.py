import tkinter as tk
import tkinter.ttk as ttk
 
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY = 33
GRAVITY = 1

class Sprite():
    def __init__(self, canvas, image_filename, x=0, y=0):
        self.image_filename = image_filename
        self.x = x
        self.y = y
        self.canvas = canvas

        self.init_canvas_object()    
        self.init_sprite()

    def init_canvas_object(self):
        self.photo_image = tk.PhotoImage(file=self.image_filename)
        self.canvas_object_id = self.canvas.create_image(
            self.x, 
            self.y,
            image=self.photo_image)

    def render(self):
        self.canvas.coords(self.canvas_object_id, self.x, self.y)

    def init_sprite(self):
        pass

    def update(self):
        pass


class GameApp(ttk.Frame): 
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(sticky="news")
        self.create_canvas()

        self.sprites = []
        self.init_game()

    def create_canvas(self):
        self.canvas = tk.Canvas(self, borderwidth=0,
            width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0)
        self.canvas.grid(sticky="news")

    def animate(self):
        for sprite in self.sprites:
            sprite.update()
            sprite.render()

        self.after(UPDATE_DELAY, self.animate)

    def start(self):
        self.after(0, self.animate)

    def init_game(self):
        pass


class Banana(Sprite):
    def init_sprite(self):
        self.vx = 0
        self.vy = 0

    def set_speed(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def update(self):
        self.x += 5
        self.y -= self.vy
        self.vy -= GRAVITY


class MonkeyGame(GameApp):
    def create_sprites(self):
        self.banana = Banana(self.canvas, 'banana.png', 100, 400)
        self.banana.set_speed(15, 25)

    def init_game(self):
        self.create_sprites()

        self.sprites.append(self.banana)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Game")
 
    # do not allow window resizing
    root.resizable(False, False)
    app = MonkeyGame(root)
    app.start()
    root.mainloop()
