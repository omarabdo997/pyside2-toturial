from PySide2.QtWidgets import QApplication, QWidget, QLabel
import sys
from PySide2.QtGui import QIcon, QPixmap


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Setting Icon")
        self.setGeometry(300,300,300,300)
        self.setIcon()
        self.setIconModes()

    def setIcon(self):
        icon = QIcon("icon.png")
        self.setWindowIcon(icon)

    def setIconModes(self):
        icon1 = QIcon("icon.png")
        label1 = QLabel("sample", self)
        pixmap1 = icon1.pixmap(100, 100, QIcon.Active, QIcon.On)
        label1.setPixmap(pixmap1)
        label2 = QLabel("sample", self)
        pixmap2 = icon1.pixmap(100, 100, QIcon.Disabled, QIcon.Off)
        label2.setPixmap(pixmap2)
        label2.move(100, 0)
        label3 = QLabel("sample", self)
        pixmap3 = icon1.pixmap(100, 100, QIcon.Selected, QIcon.On)
        label3.setPixmap(pixmap3)
        label3.move(200, 0)


myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)