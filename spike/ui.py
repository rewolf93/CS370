import tkinter as tk
import pygame as pg
import platform
import os
from car import Car


class Application(tk.Frame):
    '''
    The GUI for the architectural spike application
    '''

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_buttons()
        self.create_game_window()
        self.allgroup = pg.sprite.Group()
        self.cargroup = pg.sprite.Group()
        self.screen.fill(pg.Color(0, 150, 0))
        self.track = pg.image.load("spike/track.png")
        self.screen.blit(self.track, (50, 50))
        self.after(30, self.update)
        Car.groups = self.allgroup, self.cargroup
        pg.mixer.init()
        self.after(30, self.update)

    def create_buttons(self):
        self.button_bar = tk.Frame(self, width=200, height=600)
        self.button_bar.grid(row=0, column=0)
        self.button1 = tk.Button(self.button_bar, text="Load Car", state="normal", command=self.load_car)
        self.button1.grid(row=0)
        self.button2 = tk.Button(self.button_bar, text="Go!", state="disabled", command=self.start_button)
        self.button2.grid(row=1)
        self.button4 = tk.Button(self.button_bar, text="Play Sound", state="normal", command=self.play_sound)
        self.button4.grid(row=4)

    def create_game_window(self):
        self.game_window = tk.Frame(self, width=900, height=600)
        self.game_window.grid(row=0, column=1)

        os.environ['SDL_WINDOWID'] = str(self.game_window.winfo_id())

        if platform.system == "Windows":
            os.environ['SDL_VIDEODRIVER'] = 'windib'

        self.screen = pg.display.set_mode((900, 600))
        self.screen.fill(pg.Color(255, 255, 255))

        pg.display.init()

    def load_map(self):
        pass
        '''
        self.screen.fill(pg.Color(0, 150, 0))
        self.track = pg.image.load("spike/track.png")
        self.screen.blit(self.track, (50, 50))
        self.after(30, self.update)
        self.button1["state"] = "disabled"
        self.button2["state"] = "normal"
        '''

    def load_car(self):
        self.car = Car("spike/car.png", [195., 80])
        self.button1["state"] = "disabled"
        self.button2["state"] = "normal"
        self.redraw()

    def update(self):
        self.redraw()

    def start_button(self):
        self.car.accelerate([120, 0])
        for _ in range(325):
            self.car.move()
            self.redraw()
        self.car.accelerate([0, 0.7])
        for _ in range(255):
            self.car.move()
            self.redraw()
        self.car.accelerate([0, 0.])
        for _ in range(170):
            self.car.move()
            self.redraw()
        self.car.accelerate([0, 0.7])
        for _ in range(255):
            self.car.move()
            self.redraw()
        self.car.kill()
        self.car = Car("spike/car.png", [195., 80])
        self.redraw()

    def redraw(self):
        self.screen.fill(pg.Color(0, 150, 0))
        self.screen.blit(self.track, (50, 50))
        self.allgroup.draw(self.screen)
        pg.display.flip()

    def demo_all(self):
        self.car.x += 5
        self.update()

    def play_sound(self):
        pg.mixer.music.load("spike/free_song.mp3")
        pg.mixer.music.play(loops=0, start=180)
