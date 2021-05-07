from tkinter import *
from tkinter.ttk import Progressbar, Style
from tkinter.messagebox import showerror

import requests
import pytube


def load(root, app_root):
    # function for adding placeholder text to entry
    def add_placeholder_text(text: str, entry):
        if len(entry.get()) == 0:
            entry.insert(0, text)

    # Widget styles
    download_button_style: dict = dict(bd=0, bg="#343B48", fg="#fff", activebackground="#181818",
                                       activeforeground="#343B48", text="Download Video", compound=LEFT,
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

    output_directory_entry.bind("<FocusIn>", lambda args: output_directory_entry.delete('0', 'end'))
    output_directory_entry.bind("<FocusOut>", lambda args: add_placeholder_text("Output Directory",
                                                                                output_directory_entry))

    # file name entry
    file_name_entry = Entry(root, font=('Courier', 30))
    file_name_entry.insert(0, "File Name")
    file_name_entry.place(relx=0.125, rely=0.4, relwidth=0.75, relheigh=0.1)

    file_name_entry.bind("<FocusIn>", lambda args: file_name_entry.delete('0', 'end'))
    file_name_entry.bind("<FocusOut>", lambda args: add_placeholder_text("File Name", file_name_entry))

    # download button
    download_button = Button(root, download_button_style,
                             command=lambda: download_video(link_entry.get(), output_directory_entry.get(),
                                                            file_name_entry.get(), video_progress_bar,
                                                            video_progress_label, app_root))
    download_button.place(relx=0.25, rely=0.55, relwidth=0.5)

    # Progress bar
    video_progress_bar = Progressbar(root, orient="horizontal", length=100, mode="determinate")

    # Progress bar label
    video_progress_label = Label(root, text="0%", font=("Courier", 20), bg="#343B48", fg="#fff")

    # Gives focus to main root of app when "enter" key is pressed
    app_root.bind("<Return>", lambda args: app_root.focus_set())


def download_video(link, output, file_name, progress_bar, progress_label, root):
    progress_label.place(relx=0.375, rely=0.75, relwidth=0.25)
    progress_bar.place(relx=0.25, rely=0.7, relwidth=0.5)

    # checks to see if user is connected to the internet
    url = "https://yamiatem.github.io/YTDownloader/"
    timeout = 5

    try:
        request = requests.get(url, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
        progress_label.place_forget()
        progress_bar.place_forget()

        showerror("Error", "You are not connected to the internet")
        return

    # checks if entries are empty
    if link == "" or link == "YouTube Link":
        progress_label.place_forget()
        progress_bar.place_forget()

        showerror("Error", "All fields are required")
        return
    elif output == "" or output == "Output Directory":
        progress_label.place_forget()
        progress_bar.place_forget()

        showerror("Error", "All fields are required")
        return
    elif file_name == "" or file_name == "File Name":
        progress_label.place_forget()
        progress_bar.place_forget()

        showerror("Error", "All fields are required")
        return

    try:
        yt = pytube.YouTube(link)
    except:
        progress_label.place_forget()
        progress_bar.place_forget()

        showerror("Error", " YouTube video link is invalid")
        return

    video = yt.streams.filter(progressive=True, mime_type="video/mp4", file_extension="mp4").first()
    file_size = video.filesize

    def video_progress(chunk, file_handler, bytes_remaining):
        percent = abs(round((float(bytes_remaining)/float(file_size) * float(100)) - 100))
        print(percent)

        progress_bar['value'] = percent
        progress_label.configure(text=str(percent)+"%")

        if percent == 100:
            progress_label.configure(text="DONE!")

        root.update()

    yt.register_on_progress_callback(video_progress)

    video.download(output_path=output, filename=file_name)

    progress_label.place_forget()
    progress_bar.place_forget()
