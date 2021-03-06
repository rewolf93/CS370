import pytest

can_import_tk = True
try:
    from spike import ui
    import tkinter as tk
except ModuleNotFoundError:
    can_import_tk = False
except ImportError:
    can_import_tk = False


@pytest.fixture()
def application():
    root = tk.Tk()
    app = ui.Application(master=root)
    yield app
    root.destroy()


@pytest.mark.skipif(can_import_tk is False, reason="Cannot import tkinter")
def test_openwindow(application):
    assert application.master.winfo_exists()
