from PySide2.QtWidgets import QApplication, QWidget, QDesktopWidget
import sys
import time


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Center Widget")
        self.setGeometry(300, 300, 300, 300)
        self.center()
        
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())


myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)