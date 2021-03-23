from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit
import sys
import time


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Simple Notepad Application")
        self.setGeometry(300, 300, 300, 300)
        self.createMenu()
        textedit = QTextEdit(self)
        self.setCentralWidget(textedit)

    def createMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        viewMenu = mainMenu.addMenu("View")
        editMenu = mainMenu.addMenu("Edit")
        fontMenu = mainMenu.addMenu("Font")

        openAction = QAction("Open", self)
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.openActionSlot)
        fileMenu.addAction(openAction)
    
    def openActionSlot(self):
        print "Open Action triggered"

myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)