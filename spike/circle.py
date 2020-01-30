import tkinter as tk


class MovingCircle:

    def __init__(self, canvas, x, y, size=6, color='red'):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.circle = canvas.create_oval([x, y, x+size, y+size], outline=color, fill=color)
        self.x_vel = 0
        self.y_vel = 0

    def move(self):
        self.canvas.move(self.circle, self.x_vel, self.y_vel)
        coordinates = self.canvas.coords(self.circle)
        self.x = coordinates[0]
        self.y = coordinates[1]
