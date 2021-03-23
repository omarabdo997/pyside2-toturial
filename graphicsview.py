from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PySide2.QtGui import QBrush, QPen
from PySide2.QtCore import Qt
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Pyside2 Simple Application")
        self.setGeometry(300, 300, 300, 300)
        scene = QGraphicsScene(self)

        greenBrush = QBrush(Qt.green)
        blueBrush = QBrush(Qt.blue)

        blackPen = QPen(Qt.black)
        blackPen.setWidth(5)

        ellipse = scene.addEllipse(10, 10, 200, 200, blackPen, greenBrush)

        rect = scene.addRect(-100, -100, 200, 200, blackPen, blueBrush)

        ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        self.view = QGraphicsView(scene, self)
        self.setCentralWidget(self.view)
        self.view.rotate(30)


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)