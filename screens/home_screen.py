from tkinter import *


def load(root, app_icon):
    title_frame = Frame(root, bg="#21252B")
    title_frame.place(relx=0, rely=0, relwidth=1, height=75)

    title_label = Label(root, text="YT Downloader", bg="#21252B", fg="#fff", font=("Courier", 50))
    title_label.place(relx=0, rely=0, relwidth=1)

    icon_label = Label(root, bg="#282C34", image=app_icon)
    icon_label.place(relx=0.5, rely=0.15, anchor=N)

    app_description = Label(root, bg="#282C34", text="A python app that downloads YouTube videos", font=("Courier", 20),
                            fg="#fff")
    app_description.place(relx=0.527, rely=0.6, anchor=N)
