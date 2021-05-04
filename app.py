from tkinter import *
from tkinter.ttk import Notebook, Style

root = Tk()
root.geometry("800x600")
root.iconbitmap("icons/icon.ico")
root.title("YT Downloader")

style = Style()
style.layout('TNotebook.Tab', [])

main_frame = Frame(root, bg="#181818")
main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

title_label = Label(main_frame, bg="#ff0000", text="YT Downloader", font=("Courier", 28))
title_label.place(relx=0, rely=0, relwidth=1, relheight=0.1)
