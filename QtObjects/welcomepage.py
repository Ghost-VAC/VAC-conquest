from PySide6 import QtWidgets, QtGui
from QtObjects.gamepages.gamepage import GamePage


class WelcomePage(QtWidgets.QWidget):
    def __init__(self, surface, width, height, parent=None):
        super(WelcomePage, self).__init__(parent)
        self.surface = surface
        self.width = width
        self.height = height
        self.parent = parent
        self.setFixedSize(width, height)
        self.button = WelcomeButton("Enter game", parent=self)
        self.button.clicked.connect(self.start_game)

    def start_game(self):
        self.parent.setCentralWidget(GamePage(self.surface, self.width, self.height))


class WelcomeButton(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super(WelcomeButton, self).__init__(text=text, parent=parent)
        self.setForegroundRole(QtGui.QPalette.Dark)