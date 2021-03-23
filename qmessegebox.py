from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout
import sys
import time


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Pyside2 Simple Application")
        self.setGeometry(300, 300, 300, 300)
        self.createButton()
    
    def createButton(self):
        vbox = QVBoxLayout()
        btn1 = QPushButton("Open About Message Box")
        btn1.clicked.connect(self.aboutMessageBox)
        btn2 = QPushButton("Open Warning Message Box")
        btn2.clicked.connect(self.warningMessageBox)
        btn3 = QPushButton("Open Information Message Box")
        btn3.clicked.connect(self.informationMessageBox)
        btn4 = QPushButton("Open Question Message Box")
        btn4.clicked.connect(self.questionMessageBox)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        self.setLayout(vbox)


    def aboutMessageBox(self):
        QMessageBox.about(self, "About", "This is about message box")
    def warningMessageBox(self):
        QMessageBox.warning(self, "Warning", "This is warning message box") 
    def informationMessageBox(self):
        QMessageBox.information(self, "About", "This is information message box")
    def questionMessageBox(self):
        userInfo = QMessageBox.question(self, "Question", "This is question message box", QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            print "Yes"
        else:
            print "No"
        
myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)