import os

import requests
from PySide6.QtCore import Slot
from pytube import YouTube, exceptions


class BackEnd:
    def __init__(self, app):
        self.app = app
        self.file_size = 0
