import tkinter as tk
from ui import Application

def print_file(path):
    with open(path) as f:
        print(f.read())
        f.close()

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


main()
