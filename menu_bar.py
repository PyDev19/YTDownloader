import time
import webbrowser

from PySide6 import QtWidgets, QtGui, QtCore


class MenuBar:
    def __init__(self, parent, window, app, stacked_widget):
        self.app = app
        self.parent = parent
        self.window = window
        self.stacked_widget = stacked_widget
        self.menu_active = False

        self.menu_frame = QtWidgets.QFrame(parent)
        self.menu_frame.setObjectName("menuFrame")
        self.menu_frame.setGeometry(0, 0, 50, window.height())

        self.menu_button_frame = QtWidgets.QFrame(self.menu_frame)
        self.menu_button_layout = QtWidgets.QVBoxLayout(self.menu_button_frame)
        self.menu_button_layout.setContentsMargins(0, -1, -1, -1)

        self.menu_toggle_button = QtWidgets.QPushButton(self.menu_button_frame)
        self.menu_toggle_button.setIcon(QtGui.QPixmap("menu_icons/menu.png"))
        self.menu_toggle_button.setText("  Hide")
        self.menu_toggle_button.setObjectName("menuToggleButton")
        self.menu_toggle_button.setProperty("class", "menuButton")
        self.menu_toggle_button.setIconSize(QtCore.QSize(20, 20))
        self.menu_toggle_button.clicked.connect(lambda: self.toggle_menu())
        self.menu_button_layout.addWidget(self.menu_toggle_button)

        self.menu_home_button = QtWidgets.QPushButton(self.menu_button_frame)
        self.menu_home_button.setIcon(QtGui.QPixmap("menu_icons/home.png"))
        self.menu_home_button.setText("  Home")
        self.menu_home_button.setObjectName("menuHomeButton")
        self.menu_home_button.setProperty("class", "menuButton")
        self.menu_home_button.setIconSize(QtCore.QSize(20, 20))
        self.menu_home_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.menu_button_layout.addWidget(self.menu_home_button)

        self.menu_download_button = QtWidgets.QPushButton(self.menu_button_frame)
        self.menu_download_button.setIcon(QtGui.QPixmap("menu_icons/download.png"))
        self.menu_download_button.setText("  Download Video")
        self.menu_download_button.setObjectName("menuDownloadButton")
        self.menu_download_button.setProperty("class", "menuButton")
        self.menu_download_button.setIconSize(QtCore.QSize(20, 20))
        self.menu_download_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.menu_button_layout.addWidget(self.menu_download_button)

        self.menu_github_button = QtWidgets.QPushButton(self.menu_button_frame)
        self.menu_github_button.setIcon(QtGui.QPixmap("menu_icons/github.png"))
        self.menu_github_button.setText("  Github")
        self.menu_github_button.setObjectName("menuGithubButton")
        self.menu_github_button.setProperty("class", "menuButton")
        self.menu_github_button.setIconSize(QtCore.QSize(20, 20))
        self.menu_github_button.clicked.connect(lambda: webbrowser.open("https://github.com/PyDev19", 1, True))
        self.menu_button_layout.addWidget(self.menu_github_button)

        self.menu_repo_button = QtWidgets.QPushButton(self.menu_button_frame)
        self.menu_repo_button.setIcon(QtGui.QPixmap("menu_icons/repository.png"))
        self.menu_repo_button.setText("  Repository")
        self.menu_repo_button.setObjectName("menuRepoButton")
        self.menu_repo_button.setProperty("class", "menuButton")
        self.menu_repo_button.setIconSize(QtCore.QSize(20, 20))
        self.menu_repo_button.clicked.connect(lambda: webbrowser.open("https://github.com/PyDev19/YTDownloader", 1,
                                                                      True))
        self.menu_button_layout.addWidget(self.menu_repo_button)

        self.menu_update_button = QtWidgets.QPushButton(self.menu_button_frame)
        self.menu_update_button.setIcon(QtGui.QPixmap("menu_icons/update.png"))
        self.menu_update_button.setText("  Latest Version")
        self.menu_update_button.setObjectName("menuUpdateButton")
        self.menu_update_button.setProperty("class", "menuButton")
        self.menu_update_button.setIconSize(QtCore.QSize(20, 20))
        self.menu_update_button.clicked.connect(lambda: webbrowser.open("https://github.com/PyDev19/YTDownloader"
                                                                        "/releases", 1, True))
        self.menu_button_layout.addWidget(self.menu_update_button)

    def toggle_menu(self):
        if not self.menu_active:
            self.menu_toggle_button.setIcon(QtGui.QPixmap("menu_icons/menu_2.png"))

            for i in range(1, 7):
                width = i * 50
                self.menu_frame.setGeometry(0, 0, width, self.window.height())
                self.app.processEvents()
                time.sleep(.025)

            self.menu_active = True

        elif self.menu_active:
            self.menu_toggle_button.setIcon(QtGui.QPixmap("menu_icons/menu.png"))

            for i in range(1, 7):
                width = 350 - (i * 50)
                self.menu_frame.setGeometry(0, 0, width, self.window.height())
                self.app.processEvents()
                time.sleep(.025)

            self.menu_active = False
