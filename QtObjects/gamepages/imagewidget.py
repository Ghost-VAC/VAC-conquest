from PySide6 import QtWidgets, QtGui


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
        print(event.x(), event.y())
