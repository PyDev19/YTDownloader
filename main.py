import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine

import resources_rc

app = QGuiApplication(sys.argv)
app.setWindowIcon(QIcon(r"icons\icon.ico"))

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

sys.exit(app.exec())
