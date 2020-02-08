import tkinter as tk
from ui import Application

def print_file(path):
    with open(path) as f:
        print(f.read())
        f.close()
        
def keypress(event):
    print("pressed", repr(event.char))

def mouseclick(event):
    print("clicked at", event.x, event.y)

def main():
    root = tk.Tk()
    root.bind("<Key>", keypress)
    root.bind("<Button-1>", mouseclick)
    app = Application(master=root)
    app.mainloop()


main()
