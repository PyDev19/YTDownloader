import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine

from backend import BackEnd
import resources_rc

app = QGuiApplication(sys.argv)
app.setWindowIcon(QIcon(r"icons\icon.ico"))

backend = BackEnd(app)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')
engine.rootContext().setContextProperty('backend', backend)

sys.exit(app.exec())
