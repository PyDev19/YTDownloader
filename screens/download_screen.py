import ctypes

import requests
from PySide6 import QtWidgets, QtCore, QtGui
from pytube import YouTube, exceptions


class DownloadScreen:
    def __init__(self, stacked_widget, app):
        self.stacked_widget = stacked_widget
        self.app = app
        self.output_directory = ""

        self.download_screen_frame_layout = QtWidgets.QHBoxLayout()
        self.download_screen_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.download_screen_frame = QtWidgets.QFrame()
        self.download_screen_frame_layout.addWidget(self.download_screen_frame)

        self.entry_layout = QtWidgets.QVBoxLayout(self.download_screen_frame)
        self.entry_layout.setContentsMargins(150, -1, 150, 250)

        self.link_entry = QtWidgets.QLineEdit(self.download_screen_frame)
        self.link_entry.setPlaceholderText("YouTube Video Link")
        self.link_entry.setProperty("class", "downloadScreenEntry")
        self.entry_layout.addWidget(self.link_entry)

        self.filename_entry = QtWidgets.QLineEdit(self.download_screen_frame)
        self.filename_entry.setPlaceholderText("File Name")
        self.filename_entry.setProperty("class", "downloadScreenEntry")
        self.entry_layout.addWidget(self.filename_entry)

        self.output_button = QtWidgets.QPushButton(self.download_screen_frame)
        self.output_button.setText("Choose Output Folder")
        self.output_button.setProperty("class", "downloadScreenButton")
        self.output_button.clicked.connect(lambda: self.choose_directory())
        self.entry_layout.addWidget(self.output_button)

        self.download_button = QtWidgets.QPushButton(self.download_screen_frame)
        self.download_button.setText("Download Video")
        self.download_button.setProperty("class", "downloadScreenButton")
        self.download_button.clicked.connect(lambda: self.download_video())
        self.entry_layout.addWidget(self.download_button)

        self.progress_bar = QtWidgets.QProgressBar(self.download_screen_frame)
        self.progress_bar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progress_bar.setValue(0)
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_bar.setFont(QtGui.QFont('Times New Roman', 25))
        self.progress_bar.hide()
        self.entry_layout.addWidget(self.progress_bar)

        self.stacked_widget.addWidget(self.download_screen_frame)

    def choose_directory(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setDirectory(r"C:\Users\User\Desktop")
        self.output_directory = dialog.getExistingDirectory(None, "Select Output Folder")

    def download_video(self):
        url = "https://yamiatem.github.io/YTDownloader/"
        timeout = 5
        link = self.link_entry.text()
        file_name = self.filename_entry.text()
        output_dir = self.output_directory
        self.progress_bar.show()
        self.app.processEvents()

        try:
            request = requests.get(url, timeout=timeout)
        except (requests.ConnectionError, requests.Timeout) as exception:
            self.progress_bar.hide()
            ctypes.windll.user32.MessageBoxW(0, "You are not connected to the internet", "Error", 0)
            return

        if link == "":
            self.progress_bar.hide()
            ctypes.windll.user32.MessageBoxW(0, "Youtube link is required", "Error", 0)
            return
        elif file_name == "":
            self.progress_bar.hide()
            ctypes.windll.user32.MessageBoxW(0, "File name is required", "Error", 0)
            return
        elif file_name == "":
            self.progress_bar.hide()
            ctypes.windll.user32.MessageBoxW(0, "File name is required", "Error", 0)
            return
        elif output_dir == "":
            self.progress_bar.hide()
            ctypes.windll.user32.MessageBoxW(0, "Output directory is required", "Error", 0)
            return

        try:
            yt = YouTube(link)
        except exceptions.PytubeError as e:
            self.progress_bar.hide()
            ctypes.windll.user32.MessageBoxW(0, "YouTube video link is invalid", "Error", 0)
            return

        self.app.processEvents()

        video = yt.streams.filter(progressive=True, mime_type="video/mp4", file_extension="mp4").first()
        file_size = video.filesize

        self.app.processEvents()

        def video_progress(chunk, file_handler, bytes_remaining):
            percent = abs(round((float(bytes_remaining) / float(file_size) * float(100)) - 100))
            self.progress_bar.setValue(percent)
            self.app.processEvents()

        yt.register_on_progress_callback(video_progress)
        video.download(output_path=output_dir, filename=file_name)

        self.app.processEvents()

        self.progress_bar.reset()
        self.progress_bar.hide()
        ctypes.windll.user32.MessageBoxW(0, "Done Downloading Video!", "Info", 0)

        self.app.processEvents()
