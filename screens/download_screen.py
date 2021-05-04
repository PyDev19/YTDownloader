from tkinter import *
from tkinter.ttk import Progressbar, Style


def load(root, app_root, download_icon):
    # function for adding placeholder text to entry
    def add_placeholder_text(text: str, entry):
        if len(entry.get()) == 0:
            entry.insert(0, text)

    # Widget styles
    download_button_style: dict = dict(bd=0, bg="#ff0000", fg="#181818", activebackground="#181818",
                                       activeforeground="#ff0000", text="Download Video", image=download_icon,
                                       compound=LEFT,
                                       font=("Courier", 25))

    # YouTube link entry
    link_entry = Entry(root, font=('Courier', 30))
    link_entry.insert(0, "YouTube Link")
    link_entry.place(relx=0.125, rely=0.1, relwidth=0.75, relheigh=0.1)

    link_entry.bind("<FocusIn>", lambda args: link_entry.delete('0', 'end'))
    link_entry.bind("<FocusOut>", lambda args: add_placeholder_text("YouTube Link", link_entry))

    # output directory entry
    output_directory_entry = Entry(root, font=('Courier', 30))
    output_directory_entry.insert(0, "Output Directory")
    output_directory_entry.place(relx=0.125, rely=0.25, relwidth=0.75, relheigh=0.1)

    output_directory_entry.bind("<FocusIn>", lambda args: link_entry.delete('0', 'end'))
    output_directory_entry.bind("<FocusOut>", lambda args: add_placeholder_text("Output Directory",
                                                                                output_directory_entry))

    # download button
    download_button = Button(root, download_button_style)
    download_button.place(relx=0.25, rely=0.4, relwidth=0.5)

    # Progress bar
    video_progress_bar = Progressbar(root, orient="horizontal", length=100, mode="determinate")
    #video_progress_bar.place(relx=0.25, rely=0.55, relwidth=0.5)

    # Progress bar label
    video_progress_label = Label(root, text="0%", font=("Courier", 20), bg="#ff0000", fg="#181818")
    #video_progress_label.place(relx=0.375, rely=0.6, relwidth=0.25)

    # Gives focus to main root of app when "enter" key is pressed
    app_root.bind("<Return>", lambda args: app_root.focus_set())
