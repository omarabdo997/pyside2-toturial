from PySide2.QtWidgets import QApplication, QWidget, QDialog, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton, QGridLayout
import sys
from PySide2.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Pyside2 Grid Layout")
        self.setGeometry(300, 300, 500, 500)
        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

    def createLayout(self):
        self.groupBox = QGroupBox("Please Choose One Language  ")
        self.groupBox.setFont(QFont("Sanserif", 13))
        gridlayout = QGridLayout()
        button1 = QPushButton("CSS", self)
        gridlayout.addWidget(button1,0,0)
        button2 = QPushButton("C++", self)
        gridlayout.addWidget(button2,0,1)
        button3 = QPushButton("Java", self)
        gridlayout.addWidget(button3,1,0)
        button4 = QPushButton("JavaScript", self)
        gridlayout.addWidget(button4,1,1)

        self.groupBox.setLayout(gridlayout)


myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)