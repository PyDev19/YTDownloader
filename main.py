from tkinter import Canvas, Tk, PhotoImage
from tkinter.ttk import *
from screens import download_screen
import menu_bar

# root of app
root = Tk()

# geometry of app
x, y = round(root.winfo_screenwidth() / 5), round(root.winfo_screenheight() / 15)
root.geometry("800x600+{}+{}".format(x, y))

# title of app
root.title("YT Downloader")

# icon of app
root.iconbitmap("icons/favicon.ico")

# icons
menu_icon = PhotoImage(file="icons/menu.png")
menu_icon_2 = PhotoImage(file="icons/menu_2.png")
home_icon = PhotoImage(file="icons/home.png")
download_icon = PhotoImage(file="icons/download.png")
app_icon = PhotoImage(file="yt_downloader.png")
github_icon = PhotoImage(file="icons/github.png")
website_icon = PhotoImage(file="icons/website.png")
update_icon = PhotoImage(file="icons/update.png")

# icons array
icons = [menu_icon, menu_icon_2, home_icon, download_icon, github_icon, website_icon, update_icon]

# style
style = Style()

# theme
style.theme_use("clam")

# Style for Notebook Tabs
style.layout('TNotebook.Tab', [])

# Style for Notebook
style.layout("TNotebook", [])
style.configure("TNotebook", tabmargins=0)

# Style for main frame
style.configure("Main.TFrame", background="#282C34")

# Style for Screens
style.configure("Screens.TFrame", background="#282C34")

# Style for icon label
style.configure("Icon.TLabel", background="#282C34", image=app_icon)

# main frame of app
main = Frame(root, style="Main.TFrame")
main.pack(expand=1, fill="both")

# Notebook
tabs = Notebook(main)
tabs.pack(expand=1, fill="both")

# create screens
screen = Frame(tabs, style="Screens.TFrame")
screen.pack(expand=1, fill="both")

screen_2 = Frame(tabs, style="Screens.TFrame")
screen_2.pack(expand=1, fill="both")

# add screens
tabs.add(screen)
tabs.add(screen_2)

# load screens
icon_label = Label(screen, style="Icon.TLabel")
icon_label.pack(anchor='center')

download_screen.load(screen_2, root)

# load menu bar
menu_bar.load(main, icons, root, tabs)

root.mainloop()
