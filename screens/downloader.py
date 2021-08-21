import os

import requests
from pytube import YouTube, exceptions


class Downloader:
    def __init__(self, app, progress_bar, message_box, link_entry, filename_entry, output_entry):
        self.progress_bar = progress_bar
        self.link_entry = link_entry
        self.filename_entry = filename_entry
        self.output_entry = output_entry
        self.message_box = message_box
        self.app = app
        self.file_size = 0

    def download_video(self):
        url = "https://yamiatem.github.io/YTDownloader/"
        timeout = 5
        link = self.link_entry.text()
        file_name = self.filename_entry.text()
        file_name = file_name + ".mp4"
        output_dir = self.output_entry.text()
        self.progress_bar.show()

        try:
            request = requests.get(url, timeout=timeout)
        except (requests.ConnectionError, requests.Timeout) as exception:
            self.progress_bar.hide()
            self.message_box.setText("<strong>Error</strong>")
            self.message_box.setInformativeText("You are not connected to the internet")
            self.message_box.exec_()
            return

        if link == "":
            self.progress_bar.hide()
            self.message_box.setText("<strong>Error</strong>")
            self.message_box.setInformativeText("Youtube link is required")
            self.message_box.exec_()
            return
        elif file_name == "":
            self.progress_bar.hide()
            self.message_box.setText("<strong>Error</strong>")
            self.message_box.setInformativeText("File name is required")
            self.message_box.exec_()
            return
        elif output_dir == "":
            self.progress_bar.hide()
            self.message_box.setText("<strong>Error</strong>")
            self.message_box.setInformativeText("Output directory is required")
            self.message_box.exec_()
            return
        elif not os.path.isdir(output_dir):
            self.progress_bar.hide()
            self.message_box.setText("<strong>Error</strong>")
            self.message_box.setInformativeText("Output directory doesn't exist")
            self.message_box.exec_()

        try:
            yt = YouTube(link)
        except exceptions.PytubeError as e:
            self.progress_bar.hide()
            self.message_box.setText("<strong>Error</strong>")
            self.message_box.setInformativeText("YouTube video link is invalid")
            self.message_box.exec_()
            return

        try:
            video = yt.streams.filter(progressive=True, mime_type="video/mp4", file_extension="mp4").first()
            self.file_size = video.filesize
        except exceptions.PytubeError as e:
            self.progress_bar.hide()
            self.message_box.setText("<strong>Error</strong>")
            self.message_box.setInformativeText("Pytube Error")
            self.message_box.exec_()
            return

        yt.register_on_progress_callback(self.video_progress)
        video.download(output_path=output_dir, filename=file_name)

        self.progress_bar.reset()
        self.progress_bar.hide()

        self.message_box.setText("<b>Info</b>")
        self.message_box.setInformativeText("Done Downloading Video!")
        self.message_box.exec_()

    def video_progress(self, chunk, file_handler, bytes_remaining):
        percent = abs(round((float(bytes_remaining) / float(self.file_size) * float(100)) - 100))
        self.progress_bar.setValue(percent)
        self.app.processEvents()
