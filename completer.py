from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QCompleter, QLineEdit
import sys
import time


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Pyside2 Completer")
        self.setGeometry(300, 300, 300, 300)
        self.createCompleter()
    
    def createCompleter(self):
        vbox = QVBoxLayout()
        names = ["Afghanistan", "Argentina", "India", "Pakistan", "Japan", "Indonesia", "China", "UAE", "America",
                 "Armanistan", "Azerbaijan", "Chicago", "Chile"]
        completer = QCompleter(names)
        self.lineEdit= QLineEdit()
        self.lineEdit.setCompleter(completer)
        vbox.addWidget(self.lineEdit)
        self.setLayout(vbox)

myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)