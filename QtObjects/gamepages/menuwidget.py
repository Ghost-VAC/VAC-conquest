from PySide6 import QtWidgets, QtGui


class MenuButton(QtWidgets.QPushButton):

    def __init__(self, text, parent=None):
        """
        Defines the menu button class
        :param text: button text
        :param parent:
        """
        super(MenuButton, self).__init__(text=text, parent=parent)
        self.setForegroundRole(QtGui.QPalette.Dark)


class MenuWidget(QtWidgets.QWidget):

    def __init__(self, surface, parent=None):
        """
        Defines the menu widget of the game
        :param surface: pygame surface
        :param parent:
        """
        super(MenuWidget, self).__init__(parent)
        self.surface = surface

        menu = QtWidgets.QSplitter(QtGui.Qt.Orientation.Vertical, parent=self)
        menu.setFixedWidth(150)
        test_button = QtWidgets.QPushButton(text="Move", parent=menu)
        test_button.clicked.connect(self.shift)

        button_2 = QtWidgets.QPushButton(text="Test2", parent=menu)
        button_2.move(0, 50)

    def shift(self):
        """
        Button to move the soldier
        :return:
        """
        self.surface.soldat.move("RIGHT")