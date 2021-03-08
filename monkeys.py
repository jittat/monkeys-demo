import tkinter as tk

from gamelib import Sprite, GameApp

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

        self.monkey = Sprite(self, 'monkey.png', 50, 400)
        self.enemy = Sprite(self, 'monkey.png', 700, 400)

        self.sprites.append(self.banana)
        self.sprites.append(self.monkey)
        self.sprites.append(self.enemy)

    def init_game(self):
        self.create_sprites()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Game")
 
    # do not allow window resizing
    root.resizable(False, False)
    app = MonkeyGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
