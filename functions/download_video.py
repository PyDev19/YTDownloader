from tkinter.messagebox import *
import pytube
import requests


def download_video(link: str, file_name: str, out_dir: str):
    url = "http://www.kite.com"
    timeout = 5

    try:
        request = requests.get(url, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
        showerror("Error", "You are not connected to the internet")

    try:
        yt = pytube.YouTube(link)
    except:
        showerror("Error", " YouTube video link is invalid")

    video = yt.streams.filter(progressive=True, mime_type="video/mp4", file_extension="mp4").first()
    filesize = video.filesize

    video.download(output_path=out_dir, filename=file_name)
