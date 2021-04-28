from PySide6 import QtWidgets, QtGui


class MenuButton(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super(MenuButton, self).__init__(text=text, parent=parent)
        self.setForegroundRole(QtGui.QPalette.Dark)


class MenuWidget(QtWidgets.QWidget):
    def __init__(self, surface, parent=None):
        super(MenuWidget, self).__init__(parent)
        self.surface = surface

        menu = QtWidgets.QSplitter(QtGui.Qt.Orientation.Vertical, parent=self)
        menu.setFixedWidth(150)
        test_button = QtWidgets.QPushButton(text="Move (not working)", parent=menu)
        test_button.clicked.connect(self.sayHello)
        #test_button.setFixedSize(150, 10)

        button_2 = QtWidgets.QPushButton(text="Test2", parent=menu)
        button_2.move(0, 50)

    def sayHello(self):
        print("Move !")
        self.surface.soldat.move("RIGHT")