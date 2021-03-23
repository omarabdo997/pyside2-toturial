from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox
import sys
from PySide2.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Pyside2 QCheckBox")
        self.setGeometry(300, 300, 300, 300)
        self.createCheckBox()
    
    def createCheckBox(self):
        vbox = QVBoxLayout()
        self.label = QLabel("", self)
        check = QCheckBox("I Like Football", self)
        check.toggle()
        check.stateChanged.connect(self.checkBoxChange)
        vbox.addWidget(check)
        vbox.addWidget(self.label)
        self.setLayout(vbox)
    
    def checkBoxChange(self, state):
        if state == Qt.Checked:
            self.label.setText("Yes I like football")
        else:
            self.label.setText("No I dont like football")


myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)