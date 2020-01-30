import tkinter as tk
import random
from circle import MovingCircle

class Application(tk.Frame):
    '''
    The GUI for the architectual spike application
    '''

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.running = False
        self.pack()
        self.create_canvas()
        self.create_circle()
        self.create_widgets()

    #Creates a background to draw the circle on    
    def create_canvas(self):
        self.canvas = tk.Canvas(self, bg="black", width=250, height=250)
        self.canvas.pack()
    
    #Creates buttons to start and stop the circle
    def create_widgets(self):
        self.start_button = tk.Button(self, text="Start", command=self.start_circle)
        self.start_button.pack()
        self.stop_button = tk.Button(self, text="Stop", command=self.stop_circle, state="disabled")
        self.stop_button.pack()

    #Creates the circle
    def create_circle(self):
        self.circle = MovingCircle(self.canvas, 125, 125, size=20)

    #Starts the circle moving in a random speed and direction
    def start_circle(self):
        self.running = True
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"
        self.circle.x_vel = random.randint(-5, 5)
        self.circle.y_vel = random.randint(-5, 5)
        self.move_circle()

    #Stops the circle from moving
    def stop_circle(self):
        self.running = False
        self.stop_button["state"] = "disabled"
        self.start_button["state"] = "normal"

    #Moves the circle, and reflects it if it collides with an edge
    def move_circle(self):
        #Not sure why these numbers make it bounce correctly. I tried using circle.size and it didn't look right when it bounced.
        if self.circle.y-6 <= 0 or self.circle.y+18 >= 250:
            self.circle.y_vel = -self.circle.y_vel

        if self.circle.x-8 <= 0 or self.circle.x+18 >= 250:
            self.circle.x_vel = -self.circle.x_vel
        
        self.circle.move()

        if self.running:
            self.after(50, self.move_circle)
