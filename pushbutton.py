from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
import sys
from PySide2.QtGui import QIcon, QPixmap


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("PySide2 QPushButton")
        self.setGeometry(300,300,300,300)
        self.setIcon()
        self.setButton()

    def setIcon(self):
        icon = QIcon("icon.png")
        self.setWindowIcon(icon)
    
    def setButton(self):
        button1 = QPushButton("Quit", self)
        button1.move(50, 100)
        button1.clicked.connect(self.quitApp)
    
    def quitApp(self):
        userInfo = QMessageBox.question(self, "Confirmation", "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No)

        if userInfo == QMessageBox.Yes:
            myApp.quit()
        else:
            pass


myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)