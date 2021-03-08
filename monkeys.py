import tkinter as tk

from gamelib import Sprite, GameApp, Text

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY = 33
GRAVITY = 1

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
        self.banana = Banana(self, 'banana.png', 100, 400)
        self.banana.set_speed(15, 25)

        self.monkey = Sprite(self, 'monkey.png', 100, 400)
        self.enemy = Sprite(self, 'monkey.png', 700, 400)

        self.sprites.append(self.banana)
        self.sprites.append(self.monkey)
        self.sprites.append(self.enemy)

        self.speed_text = Text(self, 'Speed: XX', 40, 20)
        
        self.sprites.append(self.speed_text)

    def update_speed_text(self):
        self.speed_text.set_text(f'Speed: {self.speed}')
        
    def init_game(self):
        self.create_sprites()

        self.speed = 3
        self.update_speed_text()

    def on_key_pressed(self, event):
        if event.char == '+':
            if self.speed < 10:
                self.speed += 1
                self.update_speed_text()
        elif event.char == '-':
            if self.speed > 1:
                self.speed -= 1
                self.update_speed_text()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Banana Game")
 
    # do not allow window resizing
    root.resizable(False, False)
    app = MonkeyGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
