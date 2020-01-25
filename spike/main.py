import tkinter as tk
from ui import Application


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


main()
