from PySide2.QtWidgets import QApplication, QWidget, QSpinBox, QVBoxLayout, QLabel
import sys
import time


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Pyside2 SpinBox")
        self.setGeometry(300, 300, 300, 300)
        self.createSpinBox()
        self.spinValue()
       

    def createSpinBox(self):
        vbox = QVBoxLayout()
        self.label = QLabel()
        self.spinBox = QSpinBox()
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(100)
        self.spinBox.valueChanged.connect(self.spinValue)
        vbox.addWidget(self.label)
        vbox.addWidget(self.spinBox)
        self.setLayout(vbox)
    
    def spinValue(self):
        self.label.setText(str(self.spinBox.value()))

myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)