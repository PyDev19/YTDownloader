import sys

from cx_Freeze import setup, Executable

# ADD FILES
files = ['qml_components/', '__pycache__/backend.pyc', '__pycache__/resources_rc.pyc', 'icon.ico', 'main.qml']
packages = ["sys", "PySide6.QtGui", "PySide6.QtQml", "PySide6.QtCore", "pytube", "requests", "multiprocessing"]
exclude = ["tkinter", "asyncio", "concurrent", "ctypes", "distutils", 
           "lib2to3", "pydoc_data", "test", "unittest", "xmlrpc", "PySide-Addons", "PySide-Essentials"]

build_exe_options = {
    "packages": packages,
    "include_files": files,
    "excludes": exclude,
    "optimize": 2
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script="main.py",
    base=base,
    icon="icon.ico",
    targetName = "YTDownloader.exe"
)

setup (
    name="YT Downloader",
    version="3.1",
    description="Python app that downloads youtube videos",
    author="PyDev19",
    options={'build_exe': build_exe_options},
    executables=[target]
)
