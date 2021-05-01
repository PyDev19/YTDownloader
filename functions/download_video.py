from tkinter.messagebox import *
import pytube
import requests


def download_video(de, dpe, fne):
    url = "http://www.kite.com"
    timeout = 5

    link = de.get()
    out_dir = dpe.get()
    file_name = fne.get()

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
    filesize = video.filesize

    video.download(output_path=out_dir, filename=file_name)
