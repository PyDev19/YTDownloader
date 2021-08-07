from PySide6 import QtWidgets, QtCore, QtGui

from screens.downloader import Downloader


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
        self.link_entry.textChanged.connect(self.on_change_text)
        self.entry_layout.addWidget(self.link_entry)

        self.filename_entry = QtWidgets.QLineEdit(self.download_screen_frame)
        self.filename_entry.setPlaceholderText("File Name")
        self.filename_entry.setProperty("class", "downloadScreenEntry")
        self.filename_entry.textChanged.connect(self.on_change_text)
        self.entry_layout.addWidget(self.filename_entry)

        self.output_entry = QtWidgets.QLineEdit(self.download_screen_frame)
        self.output_entry.setPlaceholderText("Output Directory")
        self.output_entry.setProperty("class", "downloadScreenEntry")
        self.output_entry.textChanged.connect(self.on_change_text)
        self.entry_layout.addWidget(self.output_entry)

        self.output_button = QtWidgets.QPushButton(self.download_screen_frame)
        self.output_button.setText("Choose Output Folder")
        self.output_button.setProperty("class", "downloadScreenButton")
        self.output_button.clicked.connect(lambda: self.choose_directory())
        self.entry_layout.addWidget(self.output_button)

        self.download_button = QtWidgets.QPushButton(self.download_screen_frame)
        self.download_button.setText("Download Video")
        self.download_button.setProperty("class", "downloadScreenButton")
        self.download_button.clicked.connect(lambda: self.download_video())
        self.download_button.setDisabled(True)
        self.entry_layout.addWidget(self.download_button)

        self.progress_bar = QtWidgets.QProgressBar(self.download_screen_frame)
        self.progress_bar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progress_bar.setValue(0)
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_bar.setFont(QtGui.QFont('Times New Roman', 25))
        self.progress_bar.hide()
        self.entry_layout.addWidget(self.progress_bar)

        self.icon = QtGui.QIcon(r"icons\icon.ico")
        self.message_box = QtWidgets.QMessageBox()
        self.message_box.setWindowTitle("YT Downloader")
        self.message_box.setStyleSheet("QLabel{min-width: 300px;font-size:15pt;font-family: 'Times New Roman'}")
        self.message_box.setWindowIcon(self.icon)

        self.downloader = Downloader(self.app, self.progress_bar, self.message_box, self.link_entry, self.filename_entry
                                     , self.output_entry)
        self.stacked_widget.addWidget(self.download_screen_frame)

    def on_change_text(self):
        if self.link_entry.text() == "":
            self.download_button.setDisabled(True)
        elif self.filename_entry.text() == "":
            self.download_button.setDisabled(True)
        elif self.output_entry.text() == "":
            self.download_button.setDisabled(True)
        else:
            self.download_button.setDisabled(False)

    def choose_directory(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setDirectory(r"C:\Users\User\Desktop")
        self.output_directory = dialog.getExistingDirectory(None, "Select Output Folder")
        self.output_entry.setText(self.output_directory)

    def download_video(self):
        self.downloader.download_video()
