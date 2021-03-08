import tkinter as tk
import tkinter.ttk as ttk

class Text():
    def __init__(self, game_app, text, x=0, y=0):
        self.text = text
        self.x = x
        self.y = y
        self.canvas = game_app.canvas

        self.init_canvas_object()    
        self.init_element()

    def init_canvas_object(self):
        self.canvas_object_id = self.canvas.create_text(
            self.x, 
            self.y,
            text=self.text)

    def set_text(self, text):
        self.text = text
        self.canvas.itemconfigure(self.canvas_object_id, text=text)
        
    def render(self):
        self.canvas.coords(self.canvas_object_id, self.x, self.y)

    def init_element(self):
        pass

    def update(self):
        pass
    

class Sprite():
    def __init__(self, game_app, image_filename, x=0, y=0):
        self.image_filename = image_filename
        self.x = x
        self.y = y
        self.canvas = game_app.canvas

        self.is_visible = True

        self.init_canvas_object()    
        self.init_sprite()

    def init_canvas_object(self):
        self.photo_image = tk.PhotoImage(file=self.image_filename)
        self.canvas_object_id = self.canvas.create_image(
            self.x, 
            self.y,
            image=self.photo_image)

    def show(self):
        self.is_visible = True
        self.canvas.itemconfigure(self.canvas_object_id, state="normal")

    def hide(self):
        self.is_visible = False
        self.canvas.itemconfigure(self.canvas_object_id, state="hidden")

    def render(self):
        if self.is_visible:
            self.canvas.coords(self.canvas_object_id, self.x, self.y)

    def init_sprite(self):
        pass

    def update(self):
        pass


class GameApp(ttk.Frame): 
    def __init__(self, parent, canvas_width=800, canvas_height=500, update_delay=33):
        super().__init__(parent)
        self.parent = parent
        
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        
        self.update_delay = update_delay

        self.grid(sticky="news")
        self.create_canvas()

        self.sprites = []
        self.init_game()

        self.parent.bind('<KeyPress>', self.on_key_pressed)
        self.parent.bind('<KeyRelease>', self.on_key_released)
        
    def create_canvas(self):
        self.canvas = tk.Canvas(self, borderwidth=0,
            width=self.canvas_width, height=self.canvas_height, 
            highlightthickness=0)
        self.canvas.grid(sticky="news")

    def animate(self):
        for sprite in self.sprites:
            sprite.update()
            sprite.render()

        self.after(self.update_delay, self.animate)

    def start(self):
        self.after(0, self.animate)

    def init_game(self):
        pass

    def on_key_pressed(self, event):
        pass

    def on_key_released(self, event):
        pass
