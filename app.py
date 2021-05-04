from tkinter import *
from tkinter.ttk import Notebook, Style

root = Tk()
root.geometry("800x600")
root.iconbitmap("icons/icon.ico")
root.title("YT Downloader")

style = Style()
style.layout('TNotebook.Tab', [])

tabs = Notebook(root)
tabs.pack(fill='both', expand=1)

# screens
home_screen = Canvas(root, bg="#181818")
home_screen.pack(fill='both', expand=1)

# added screens
tabs.add(home_screen)
