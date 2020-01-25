import pytest
import tkinter as tk
from spike import ui


@pytest.fixture()
def application():
    root = tk.Tk()
    app = ui.Application(master=root)
    yield app
    root.destroy()


def test_openwindow(application):
    assert application.master.winfo_exists()
