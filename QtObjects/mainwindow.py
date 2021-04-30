from PySide6 import QtWidgets

from QtObjects.welcomepage import WelcomePage
from QtObjects.gamepages.gamepage import GamePage


class MainWindow(QtWidgets.QMainWindow):
    # https://doc.qt.io/qtforpython/PySide6/QtWidgets/QMainWindow.html#qt-main-window-framework
    def __init__(self, surface, x0, y0, width, height, parent=None):
        """
        Defines the main window of the game
        :param surface: the pygame surface
        :param x0: initial position on screen
        :param y0: initial position on screen
        :param width: int
        :param height: int
        :param parent: parent
        """
        super(MainWindow, self).__init__(parent)
        self.setGeometry(x0, y0, width, height)
        self.setWindowTitle("VAC-Conquest")

        self.currentCentralWidget = WelcomePage(surface, width, height, self)
        self.setCentralWidget(self.currentCentralWidget)

    def refresh(self, screen):
        """
        Refreshes the pygame window
        Must be called at any animation
        :param screen: game screen
        :return: None
        """
        self.currentCentralWidget = GamePage(screen, width=300, height=500)
        self.setCentralWidget(screen.window.currentCentralWidget)