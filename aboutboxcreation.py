from PySide2.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox, QPushButton
import sys
import time
from PySide2.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("About Box Creation")
        self.setGeometry(300, 300, 300, 300)
        self.center()
        self.pushButton()
        self.setIcon()
        
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
    
    def aboutBox(self):
        QMessageBox.about(self.aboutButton, "About", "About text")

    def pushButton(self):
        self.aboutButton = QPushButton("Open About Box", self)
        self.move(50, 100)
        self.aboutButton.clicked.connect(self.aboutBox)

    def setIcon(self):
        icon = QIcon("icon.png")
        self.setWindowIcon(icon)



myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)