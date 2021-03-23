from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QPen, QBrush, QPolygon
from PySide2.QtCore import Qt, QPoint
import sys


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Pyside2 Simple Application")
        self.setGeometry(300, 300, 800, 600)
        

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.blue, 7, Qt.DashDotLine))
        painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))

        painter.drawEllipse(100, 100, 400, 200)

        points = QPolygon([
            QPoint(10, 10),
            QPoint(10, 100),
            QPoint(100, 100),
            QPoint(100, 10),
            
        ])

        painter.drawPolygon(points)

myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)