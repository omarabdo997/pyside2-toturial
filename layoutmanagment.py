from PySide2.QtWidgets import QApplication, QWidget, QDialog, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton
import sys
from PySide2.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Pyside2 Simple Application")
        self.setGeometry(300, 300, 500, 500)
        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

    def createLayout(self):
        self.groupBox = QGroupBox("Please Choose One Language  ")
        self.groupBox.setFont(QFont("Sanserif", 13))
        hbox = QHBoxLayout()
        button1 = QPushButton("CSS", self)
        hbox.addWidget(button1)
        button2 = QPushButton("C++", self)
        hbox.addWidget(button2)
        button3 = QPushButton("Java", self)
        hbox.addWidget(button3)

        self.groupBox.setLayout(hbox)


myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)