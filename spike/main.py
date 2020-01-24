import tkinter as tk


class Application(tk.Frame):
    '''
    The GUI for the architectual spike application
    '''

    def __init__(self, master=None):
        super().__init__(master)


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


main()
