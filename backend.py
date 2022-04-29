import os

import requests
from PySide6.QtCore import Slot, QObject
from pytube import YouTube, exceptions

class BackEnd(QObject):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.file_size = 0
    
    @Slot(result=bool)
    def check_internet(self): 
        url = "https://yamiatem.github.io/YTDownloader/"
        timeout = 5

        try:
            request = requests.get(url, timeout=timeout)
            return False
        except (requests.ConnectionError, requests.Timeout) as exception:
            return True
