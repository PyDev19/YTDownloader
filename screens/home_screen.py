from PySide6 import QtGui, QtWidgets, QtCore


class HomeScreen:
    def __init__(self, stacked_widget):
        self.stacked_widget = stacked_widget

        self.icon = QtGui.QPixmap("icons/icon-512x512.png")
        self.image = QtWidgets.QLabel()
        self.image.setPixmap(self.icon)
        self.image.setAlignment(QtCore.Qt.AlignCenter)

        self.stacked_widget.addWidget(self.image)
