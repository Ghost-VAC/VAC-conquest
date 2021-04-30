from PySide6 import QtWidgets, QtGui
from QtObjects.gamepages.gamepage import GamePage


class WelcomePage(QtWidgets.QWidget):

    def __init__(self, surface, width, height, parent=None):
        """
        Defines the welcome page of the game
        :param surface: pygame surface
        :param width: int
        :param height: int
        :param parent:
        """
        super(WelcomePage, self).__init__(parent)
        self.surface = surface
        self.width = width
        self.height = height
        self.parent = parent
        self.setFixedSize(width, height)
        self.button = WelcomeButton("Enter game", parent=self)
        self.button.clicked.connect(self.start_game)

    def start_game(self):
        """
        Starts the game
        Called when clicked on the start button
        :return: None
        """
        self.parent.currentCentralWidget = GamePage(self.surface, self.width, self.height)
        self.parent.setCentralWidget(self.parent.currentCentralWidget)


class WelcomeButton(QtWidgets.QPushButton):

    def __init__(self, text, parent=None):
        """
        Creates the button to enter the game
        :param text: The text to be displayed on the button
        :param parent:
        """
        super(WelcomeButton, self).__init__(text=text, parent=parent)
        self.setForegroundRole(QtGui.QPalette.Dark)