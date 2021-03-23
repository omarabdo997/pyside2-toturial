from PySide2.QtWidgets import QApplication, QMainWindow, QStatusBar
import sys
import time


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Status Bar")
        self.setGeometry(300, 300, 300, 300)
        self.createStatusBar()

    def createStatusBar(self):
        self.myStatus = QStatusBar()
        self.myStatus.showMessage("hello", 3000)
        self.setStatusBar(self.myStatus)

myApp = QApplication(sys.argv)
window = Window()
window.show()




myApp.exec_()
sys.exit(0)