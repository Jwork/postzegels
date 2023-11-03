import tkinter as tk
import tkinter.ttk as ttk
import ui.menu
import ui.form
import tksvg

def setupUI() -> None:
    root = tk.Tk()
    root.title("Cata log")
    root.geometry('{}x{}'.format(460, 350))
    
    app_icon = tksvg.SvgImage(file="resources/icons/stamp.svg", height=300, width=300)
    root.iconphoto(False, app_icon)


    ui.menu.createMenu(root)
    ui.form.render(root)

    root.mainloop()