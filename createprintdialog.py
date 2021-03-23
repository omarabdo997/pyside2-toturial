from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit
import sys
from PySide2.QtGui import QIcon, QFont
from PySide2.QtPrintSupport import QPrinter, QPrintPreviewDialog, QPrintDialog


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Simple Notepad Application")
        self.setGeometry(300, 300, 300, 300)
        self.createMenu()
        self.textedit = QTextEdit(self)
        self.setCentralWidget(self.textedit)

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

        previewAction = QAction("Print Preview", self)
        previewAction.triggered.connect(self.print_preview_dialog)

        printAction = QAction("Print", self)
        printAction.triggered.connect(self.printDialog)

        viewMenu.addAction(previewAction)
        viewMenu.addAction(printAction)
    
    def openActionSlot(self):
        print "Open Action triggered"

    def print_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec_()
    
    def print_preview(self, printer):
        self.textedit.print_(printer)
    
    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textedit.print_(printer)

myApp = QApplication(sys.argv)
window = Window()
window.show()


myApp.exec_()
sys.exit(0)