from PySide6 import QtWidgets
import pygame
import sys

from QtObjects.mainwindow import MainWindow

from pygamewindow import PygameWindow

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    pygame.init()

    surface = PygameWindow((640, 480))

    main_window = MainWindow(surface, 300, 100, 640, 480)
    surface.window = main_window
    main_window.show()

    sys.exit(app.exec_())