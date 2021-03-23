from PySide2.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit, QAction
import sys
import time


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Pyside2 Simple Application")
        self.setGeometry(300, 300, 300, 300)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        menu_bar = self.menuBar()
        file = menu_bar.addMenu("File")
        new = QAction("New", self)
        new.triggered.connect(self.newSlot)
        file.addAction(new)
        cascade = QAction("Cascade", self)
        cascade.triggered.connect(self.cascadeAction)
        file.addAction(cascade)
        tiled = QAction("Tiled", self)
        tiled.triggered.connect(self.tileAction)
        file.addAction(tiled)
        self.count = 0

    def newSlot(self):
        self.count += 1
        sub = QMdiSubWindow()
        sub.setWidget(QTextEdit())
        sub.setWindowTitle("Sub Window " + str(self.count))
        self.mdi.addSubWindow(sub)
        sub.show()
    
    def cascadeAction(self):
        self.mdi.cascadeSubWindows()
    
    def tileAction(self):
        self.mdi.tileSubWindows()


myApp = QApplication(sys.argv)
window = Window()
window.show()




myApp.exec_()
sys.exit(0)