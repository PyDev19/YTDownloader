from tkinter import *
from tkinter.ttk import Notebook, Style

root = Tk()
root.geometry("800x600")
root.iconbitmap("icons/icon.ico")
root.title("YT Downloader")

menu_icon = PhotoImage(file="images/menu.png")
nav_bar_active = False


def open_nav_menu():
    global nav_bar_active
    print(nav_bar_active)

    if not nav_bar_active:
        for i in range(-1000, 1):
            print(i)
            nav_frame.place(x=i)
            main_frame.update()

        nav_bar_active = True
    else:
        for i in range(1001):
            print(-i)
            nav_frame.place(x=-i)
            main_frame.update()

        nav_bar_active = False

    print(nav_bar_active)


style = Style()
style.layout('TNotebook.Tab', [])

main_frame = Frame(root, bg="#181818")
main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

title_frame = Frame(main_frame, bg="#181818")
title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)

title_label = Label(title_frame, bg="#ff0000", text="YT Downloader", font=("Courier", 28))
title_label.place(relx=0, rely=0, relwidth=1, relheight=1)

nav_button = Button(title_frame, image=menu_icon, bg="#ff0000", bd=0, activebackground="#181818",
                    command=lambda: open_nav_menu())
nav_button.place(relx=0, relheight=1)

nav_frame = Frame(main_frame, bg="#ff0000")
nav_frame.place(x=-1000, rely=0.1, relwidth=0.25, relheight=0.90)

download_button = Button(nav_frame, bg="#181818", fg="#ff0000", activebackground="#ff0000", activeforeground="#181818",
                         text="Download", bd=0, font=("Courier", 25))
download_button.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.1)

convert_button = Button(nav_frame, bg="#181818", fg="#ff0000", activebackground="#ff0000", activeforeground="#181818",
                        text="Convert", bd=0, font=("Courier", 25))
convert_button.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.1)

settings_button = Button(nav_frame, bg="#181818", fg="#ff0000", activebackground="#ff0000", activeforeground="#181818",
                         text="Settings", bd=0, font=("Courier", 25))
settings_button.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.1)
