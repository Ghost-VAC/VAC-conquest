from PySide6 import QtWidgets

from QtObjects.gamepages.menuwidget import MenuWidget
from QtObjects.gamepages.imagewidget import ImageWidget


class GamePage(QtWidgets.QSplitter):

    def __init__(self, surface, width, height):
        """
        Initialize the game page
        Includes the menu and the game image
        :param surface: pygame game surface
        :param width:
        :param height:
        """
        super(GamePage, self).__init__()
        self.width = width
        self.height = height
        self.setFixedSize(width, height)

        self.image = ImageWidget(surface, self)
        self.menu = MenuWidget(surface, self)