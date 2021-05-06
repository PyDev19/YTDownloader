from tkinter import *
from tkinter.ttk import Notebook, Style
from screens import download_screen
from screens import home_screen

import webbrowser

# root of app
root = Tk()

# title of app
root.title("YT Downloader")

# icon of app
root.iconbitmap("icons/icon.ico")

# geometry of app
x, y = round(root.winfo_screenwidth() / 5), round(root.winfo_screenheight() / 15)
root.geometry("800x600+{}+{}".format(x, y))

# icons
menu_icon = PhotoImage(file="icons/menu.png")
home_icon = PhotoImage(file="icons/home.png")
download_icon = PhotoImage(file="icons/download.png")
app_icon = PhotoImage(file="images/yt_downloader.png")
github_icon = PhotoImage(file="icons/github.png")
website_icon = PhotoImage(file="icons/website.png")
update_icon = PhotoImage(file="icons/update.png")

# dicts of widgets
menu_buttons_style: dict = dict(compound=LEFT, bd=0, bg="#21252B", fg="#fff", font=("Courier", 20),
                                activebackground="#BD93F9", anchor="w", padx=20, width=300)

# toggle menu bool
menu_active: bool = False


# open and close of menu
def toggle_menu():
    global menu_active

    if not menu_active:
        for i in range(int(58.4), 301, 5):
            menu_frame.place(width=i)
            root.update()

        menu_active = True
    elif menu_active:
        for i in range(300, int(56), -3):
            menu_frame.place(width=i)
            root.update()

        menu_active = False


# Style
style = Style()

# Style for Notebook Tabs
style.layout('TNotebook.Tab', [])

# Style for Notebook
style.layout("TNotebook", [])
style.configure("TNotebook", tabmargins=0)

# main frame of app
main = Frame(root, bg="#282C34")
main.pack(expand=1, fill="both")

# Notebook
tabs = Notebook(main)
tabs.pack(expand=1, fill="both", side="right")

# create screens
screen = Frame(tabs, bg="#282C34")
screen.pack(expand=1, fill="both")

screen_2 = Frame(tabs, bg="#282C34")
screen_2.pack(expand=1, fill="both")

screen_3 = Frame(tabs, bg="#282C34")
screen_3.pack(expand=1, fill="both")

# add screens
tabs.add(screen)
tabs.add(screen_2)
tabs.add(screen_3)

# load screens
home_screen.load(screen, app_icon)
download_screen.load(screen_2, root)

# menu frame
menu_frame = Frame(main, bg="#21252B")
menu_frame.place(relx=0, rely=0, relheight=1, width=58.4)

# menu button
menu_button = Button(menu_frame, menu_buttons_style, image=menu_icon, text="Hide", command=lambda: toggle_menu())
menu_button.grid(column=0, row=0)

# home button
home_button = Button(menu_frame, menu_buttons_style, image=home_icon, text="Home", command=lambda: tabs.select(0))
home_button.grid(column=0, row=1)

# download button
download_button = Button(menu_frame, menu_buttons_style, image=download_icon, text="Download",
                         command=lambda: tabs.select(1))
download_button.grid(column=0, row=2)

# github button
github_button = Button(menu_frame, menu_buttons_style, image=github_icon, text="GitHub",
                       command=lambda: webbrowser.open("https://github.com/YamiAtem/YTDownloader", new=0,
                                                       autoraise=True))
github_button.grid(column=0, row=3)

# website button
website_button = Button(menu_frame, menu_buttons_style, image=website_icon, text="App Website",
                        command=lambda: webbrowser.open("https://yamiatem.github.io/YTDownloader/", new=0,
                                                        autoraise=True))
website_button.grid(column=0, row=4)

# update button
update_button = Button(menu_frame, menu_buttons_style, image=update_icon, text="Latest Update",
                       command=lambda: webbrowser.open("https://github.com/YamiAtem/YTDownloader/releases",
                                                       new=0, autoraise=True))
update_button.grid(column=0, row=5)

root.mainloop()
