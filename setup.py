import sys
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icons/favicon.ico', 'icons/', 'menu_bar.py', 'yt_downloader.png', 'screens/']

build_exe_options = {"packages": ["os"], 'include_files': files}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script="main.py",
    base=base,
    icon="icons/favicon.ico"
)

setup(
    name="Test",
    version="1.0",
    description="Test",
    author="Test",
    options={'build_exe': build_exe_options},
    executables=[target]
)
