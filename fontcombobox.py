from PySide2.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QFontComboBox
import sys
import time


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Pyside2 FontCombo Box")
        self.setGeometry(300, 300, 300, 300)
        self.setFontComboBox()
        self.fontComboBox.currentFontChanged.connect(self.printTheCurrentFont)

    def setFontComboBox(self):
        vbox = QVBoxLayout()
        self.fontComboBox = QFontComboBox()
        vbox.addWidget(self.fontComboBox)
        self.setLayout(vbox)
    
    def printTheCurrentFont(self):
        font = self.fontComboBox.currentFont
        print font

myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)