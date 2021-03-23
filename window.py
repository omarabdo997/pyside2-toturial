from PySide2.QtWidgets import QApplication, QWidget
import sys
import time


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Pyside2 Simple Application")
        self.setGeometry(300, 300, 300, 300)
        # self.setMinimumHeight(100)
        # self.setMinimumWidth(250)
        # self.setMaximumHeight(200)
        # self.setMaximumWidth(300)


myApp = QApplication(sys.argv)
window = Window()
window.show()

time.sleep(5)
window.resize(500, 500)


myApp.exec_()
sys.exit(0)