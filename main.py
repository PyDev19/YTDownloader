from tkinter import *
from tkinter.ttk import Notebook, Style
from screens import download_screen

# root of app
root = Tk()
root.geometry("800x600")
root.iconbitmap("icons/icon.ico")
root.title("YT Downloader")

# icons
menu_icon = PhotoImage(file="images/menu.png")
download_icon = PhotoImage(file="images/download.png")

nav_bar_active = False


# Function for opening and closing menu
def nav_menu():
    global nav_bar_active
    print(nav_bar_active)

    if not nav_bar_active:
        nav_bar_active = True
        for i in range(-1000, 1):
            print(i)
            nav_frame.place(x=i)
            main_frame.update()

        tabs.place(relx=0.25, relwidth=0.75)
    else:
        nav_bar_active = False
        for i in range(1001):
            print(-i)
            nav_frame.place(x=-i)
            main_frame.update()

        tabs.place(relx=0, relwidth=1)

    print(nav_bar_active)


# Style
style = Style()

# Style for Notebook Tabs
style.layout('TNotebook.Tab', [])

# Style for Notebook
style.layout("TNotebook", [])
style.configure("TNotebook", tabmargins=0)

# The Main Frame of Program
main_frame = Frame(root, bg="#181818")
main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# Created Notebook
tabs = Notebook(main_frame)
tabs.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

# Created Screens
home_screen = Frame(tabs, bg="#181818")
home_screen.place(relx=0, rely=0, relwidth=1, relheight=1)

convert_screen = Frame(tabs, bg="#00ff00")
convert_screen.place(relx=0, rely=0, relwidth=1, relheight=1)

settings_screen = Frame(tabs, bg="#0000ff")
settings_screen.place(relx=0, rely=0, relwidth=1, relheight=1)

# Added Screens
tabs.add(home_screen)
tabs.add(convert_screen)
tabs.add(settings_screen)

# Load Screens
download_screen.load(home_screen, root, download_icon)

# Frame for Menu Button and Tittle
title_frame = Frame(main_frame, bg="#181818")
title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)

# Label Tittle
title_label = Label(title_frame, bg="#ff0000", text="YT Downloader", font=("Courier", 40))
title_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# Button for Menu
nav_button = Button(title_frame, image=menu_icon, bg="#ff0000", bd=0, activebackground="#181818",
                    command=lambda: nav_menu())
nav_button.place(relx=0, relheight=1)

# Frame of Menu
nav_frame = Frame(main_frame, bg="#ff0000")
nav_frame.place(x=-1000, rely=0.1, relwidth=0.25, relheight=0.90)

# Button for Download Screens
download_button = Button(nav_frame, bg="#181818", fg="#ff0000", activebackground="#ff0000", activeforeground="#181818",
                         text="Download", bd=0, font=("Courier", 25), command=lambda: tabs.select(0))
download_button.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.1)

# Button for Convert Screen
convert_button = Button(nav_frame, bg="#181818", fg="#ff0000", activebackground="#ff0000", activeforeground="#181818",
                        text="Convert", bd=0, font=("Courier", 25), command=lambda: tabs.select(1))
convert_button.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.1)

# Button for Settings Screen
settings_button = Button(nav_frame, bg="#181818", fg="#ff0000", activebackground="#ff0000", activeforeground="#181818",
                         text="Settings", bd=0, font=("Courier", 25), command=lambda: tabs.select(2))
settings_button.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.1)

root.mainloop()
