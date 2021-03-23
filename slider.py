from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QSlider
import sys
import time
from PySide2.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Pyside2 Slider")
        self.setGeometry(300, 300, 300, 300)
        self.setStyleSheet("background-color:red")
        self.createSlider()
    
    def createSlider(self):
        hbox = QHBoxLayout()
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.label = QLabel("0")
        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)
        self.setLayout(hbox)
        self.slider.valueChanged.connect(self.sliderGetValue)

    
    def sliderGetValue(self):
        print self.slider.value()
        self.label.setText(str(self.slider.value()))

myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)