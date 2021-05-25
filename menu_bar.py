from tkinter import Tk
import webbrowser
from tkinter.ttk import *
from tkinter.constants import *

# toggle menu bool
menu_active: bool = False


def load(main, icons: list, root, notebook):
    # style
    style = Style()

    # style for menu frame
    style.configure("Menu.TFrame", background="#21252B")

    # style for menu buttons
    style.configure("Menu.TButton", relief=FLAT, font=("Times New Roman", 20), anchor="w", width=21, foreground="#fff",
                    padding='12 1 1 1')
    style.map("Menu.TButton", background=[("pressed", "#BD93F9"), ("!active", "#21252B"), (ACTIVE, "#282C34")])

    # menu frame
    menu_frame = Frame(main, style="Menu.TFrame")
    menu_frame.place(relx=0, rely=0, relheight=1, width=50)

    # menu button
    menu_button = Button(menu_frame, style="Menu.TButton", image=icons[0], compound=LEFT, text="  Hide",
                         takefocus=False,
                         command=lambda: toggle_menu(root, menu_frame, menu_button, icons))
    menu_button.grid(column=0, row=0)

    # home button
    home_button = Button(menu_frame, style="Menu.TButton", image=icons[2], compound=LEFT, text="  Home",
                         takefocus=False, command=lambda: select_screen(notebook, 0, icons, root, menu_frame,
                                                                        menu_button))
    home_button.grid(column=0, row=1)

    # download button
    download_button = Button(menu_frame, style="Menu.TButton", image=icons[3], compound=LEFT, text="  Download Video",
                             takefocus=False, command=lambda: select_screen(notebook, 1, icons, root, menu_frame,
                                                                            menu_button))
    download_button.grid(column=0, row=2)

    # github button
    github_button = Button(menu_frame, style="Menu.TButton", image=icons[4], text="  GitHub", compound=LEFT,
                           command=lambda: webbrowser.open("https://github.com/YamiAtem/YTDownloader", new=0,
                                                           autoraise=True))
    github_button.grid(column=0, row=3)

    # update button
    update_button = Button(menu_frame, style="Menu.TButton", image=icons[5], text="  Latest Update", compound=LEFT,
                           command=lambda: webbrowser.open("https://github.com/YamiAtem/YTDownloader/releases",
                                                           new=0, autoraise=True))
    update_button.grid(column=0, row=4)


# open and close of menu
def toggle_menu(root: Tk, menu_frame: Frame, menu_button: Button, icons: list):
    global menu_active

    if not menu_active:
        menu_button.configure(image=icons[1])

        for i in range(1, 7):
            width = i * 50
            menu_frame.place(width=width)
            root.update()

        menu_active = True
    elif menu_active:
        menu_button.configure(image=icons[0])

        for i in range(1, 7):
            width = 350 - (i * 50)
            menu_frame.place(width=width)
            root.update()

        menu_active = False


# switch screens
def select_screen(tabs, index, icons, root, menu_frame, menu_button):
    global menu_active

    tabs.select(index)

    if menu_active:
        menu_button.configure(image=icons[0])

        for i in range(1, 7):
            width = 350 - (i * 50)
            menu_frame.place(width=width)
            root.update()

        menu_active = False
