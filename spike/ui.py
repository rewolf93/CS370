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
        self.startpos = (150, 150)
        self.grid()
        self.create_buttons()
        self.create_game_window()
        self.allgroup = pg.sprite.Group()
        self.cargroup = pg.sprite.Group()
        Car.groups = self.allgroup, self.cargroup
        self.after(30, self.update)

    def create_buttons(self):
        self.button_bar = tk.Frame(self, width=200, height=600)
        self.button_bar.grid(row=0, column=0)
        self.button1 = tk.Button(self.button_bar, text="Load Map", command=self.load_map)
        self.button1.grid(row=0)
        self.button2 = tk.Button(self.button_bar, text="Load Car", state="disabled", command=self.load_car)
        self.button2.grid(row=1)
        self.button3 = tk.Button(self.button_bar, text="Go!", state="disabled", command=self.start_button)
        self.button3.grid(row=3)

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
        self.screen.fill(pg.Color(0, 150, 0))
        self.track = pg.image.load("track.png")
        self.screen.blit(self.track, (50, 50))
        self.after(30, self.update)
        self.button1["state"] = "disabled"
        self.button2["state"] = "normal"

    def load_car(self):
        self.car = Car("car.png", self.startpos)
        self.after(30, self.update)
        self.button2["state"] = "disabled"
        self.button3["state"] = "normal"

    def update(self):
        self.screen.fill(pg.Color(0, 150, 0))
        self.screen.blit(self.track, (50, 50))
        self.allgroup.update()
        self.allgroup.draw(self.screen)
        pg.display.flip()

    def start_button(self):
        self.car.x += 5
        self.update()
