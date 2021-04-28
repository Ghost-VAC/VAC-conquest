from PySide6 import QtWidgets

from QtObjects.welcomepage import WelcomePage


class MainWindow(QtWidgets.QMainWindow):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMainWindow.html#qt-main-window-framework
    def __init__(self, surface, x0, y0, width, height, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(x0, y0, width, height)
        self.setWindowTitle("VAC-Conquest")

        self.setCentralWidget(WelcomePage(surface, width, height, self))
