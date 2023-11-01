import tkinter as tk
import tkinter.ttk as ttk
import ui.menu
import ui.form


def setupUI() -> None:
    root = tk.Tk()

    ui.menu.createMenu(root)
    ui.form.renderForm()

    root.mainloop()