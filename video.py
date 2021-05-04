from tkinter.messagebox import *
import pytube
import requests
import app


def download_video(download_entry, download_path_entry, file_name_entry, progress_bar, progress_label):
    url = "https://yamiatem.github.io/YTDownloader/"
    timeout = 5

    link = download_entry.get()
    out_dir = download_path_entry.get()
    file_name = file_name_entry.get()

    try:
        request = requests.get(url, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
        showerror("Error", "You are not connected to the internet")
        return

    try:
        yt = pytube.YouTube(link)
    except:
        showerror("Error", " YouTube video link is invalid")
        return

    video = yt.streams.filter(progressive=True, mime_type="video/mp4", file_extension="mp4").first()

    def progress_check(chunk, file_handle, bytes_remaining):
        percent = round((float(bytes_remaining) / float(video.filesize)) * float(100))

        progress_bar['value'] = 100 - percent
        progress_label.configure(text=str(100 - percent) + "%")

        app.root.update()

    yt.register_on_progress_callback(progress_check)

    video.download(output_path=out_dir, filename=file_name)

    progress_bar['value'] = 0
    progress_label.configure(text="0%")
