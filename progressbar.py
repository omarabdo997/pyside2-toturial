from PySide2.QtWidgets import QApplication, QMainWindow, QProgressBar, QStatusBar, QLabel
import sys
import time


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Progress Bar")
        self.setGeometry(300, 300, 300, 300)
        self.statusLabel = QLabel("showing progress")
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(20)
        self.createStatusBar()
       

    def createStatusBar(self):
        self.statusBar = QStatusBar()

        self.statusBar.addWidget(self.statusLabel, 1)
        self.statusBar.addWidget(self.progressBar, 2)
        self.setStatusBar(self.statusBar)

myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)