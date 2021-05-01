from tkinter import *
from tkinter.ttk import Progressbar, Style
import app


def load(root):
    style = Style()
    style.configure("red.Vertical.TProgressbar", foreground='white', background='red')

    def add_placeholder_text(text: str, entry):
        if len(entry.get()) == 0:
            entry.insert(0, text)

    title_label = Label(root, bg='#ff0000', fg="#fff", text="YT DOWNLOADER", justify=CENTER,
                        font=('Courier New', 40, 'bold'))
    title_label.pack(fill='x', side=TOP)

    download_entry = Entry(root, font=('Courier New', 20))
    download_entry.insert(0, 'YouTube Link')
    download_entry.place(relx=0.01, rely=0.125, relheight=0.075, relwidth=0.6)

    download_entry.bind("<FocusIn>", lambda args: download_entry.delete('0', 'end'))
    download_entry.bind("<FocusOut>", lambda args: add_placeholder_text("YouTube Link", download_entry))

    download_path_entry = Entry(root, font=('Courier New', 20))
    download_path_entry.insert(0, 'Output path')
    download_path_entry.place(relx=0.01, rely=0.25, relheight=0.075, relwidth=0.6)

    download_path_entry.bind("<FocusIn>", lambda args: download_path_entry.delete('0', 'end'))
    download_path_entry.bind("<FocusOut>", lambda args: add_placeholder_text('Output path', download_path_entry))

    file_name_entry = Entry(root, font=('Courier New', 20))
    file_name_entry.insert(0, 'File Name')
    file_name_entry.place(relx=0.01, rely=0.375, relheight=0.075, relwidth=0.6)

    file_name_entry.bind("<FocusIn>", lambda args: file_name_entry.delete('0', 'end'))
    file_name_entry.bind("<FocusOut>", lambda args: add_placeholder_text('File Name', file_name_entry))

    download_progress_bar = Progressbar(root, orient=VERTICAL, length=100, mode='determinate')
    download_progress_bar.place(relx=0.675, rely=0.125, relheight=0.75, relwidth=0.25)

    app.root.bind("<Return>", lambda args: app.root.focus_set())
