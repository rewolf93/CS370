import tkinter as tk
from ui import Application

def print_file():
    f = open("inputfile.txt", "r")
    print(f.read())
    f.close()

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


main()
