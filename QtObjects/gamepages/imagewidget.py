from PySide6 import QtWidgets, QtGui
import math

class ImageWidget(QtWidgets.QWidget):

    def __init__(self, surface, parent=None):
        """
        Defines the image widget containing the pygame window
        :param surface: pygame window
        :param parent:
        """
        super(ImageWidget, self).__init__(parent)
        w = surface.get_width()
        h = surface.get_height()
        self.surface = surface
        self.data = surface.get_buffer().raw
        self.image = QtGui.QImage(self.data, w, h, QtGui.QImage.Format_RGB32)

    def paintEvent(self, event):
        """
        Paints the pygame window
        :param event:
        :return:
        """
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.image)
        qp.end()

    def mousePressEvent(self, event):
        """
        The event triggered when the mouse is pressed over the widget
        :param event:
        :return:
        """

        def fy(y):
            return round(2*y/(3*r) - 1)

        def fx(x):
            return round(x/(r*math.sqrt(3)) - 1 - (y%2==0)*0.5)

        r = self.surface.case_radius
        print(event.x(), event.y())
        y = fy(event.y())
        x = fx(event.x())
        case = self.surface.board.cases[y][x]
        print(x,y)
        if case.occupant:
            print(case.occupant.possible_cases())
