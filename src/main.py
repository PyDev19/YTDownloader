import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine

from src.backend import BackEnd
import src.resources_rc

app = QGuiApplication(sys.argv)
app.setWindowIcon(QIcon(r"icon.ico"))

backend = BackEnd(app)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('src/main.qml')
engine.rootContext().setContextProperty('backend', backend)

sys.exit(app.exec())
