import sys

from cx_Freeze import setup, Executable

# ADD FILES
files = ['qml_components/', 'backend.py', 'resources_rc.py', 'menu_icons/', 'icons/', 'main.qml']
packages = ["sys", "PySide6.QtGui", "PySide6.QtQml", "PySide6.QtCore", "pytube", "requests"]
exclude = ["tkinter", "asyncio", "concurrent", "ctypes", "distutils", 
           "email", "html", "http", "lib2to3", "multiprocessing", 
           "pydoc_data", "test", "unittest", "xml", "xmlrpc"]

build_exe_options = {
    "packages": packages,
    "include_files": files,
    "excludes": exclude
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script="main.py",
    base=base,
    icon="icons/icon.ico"
)

setup(
    name="YT Downloader",
    version="3.1",
    description="Python app that downloads youtube videos",
    author="PyDev19",
    options={'build_exe': build_exe_options},
    executables=[target]
)
