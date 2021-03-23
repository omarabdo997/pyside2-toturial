from PySide2.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout
import sys
import time


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("QCalendar Widget Application")
        self.setGeometry(300, 300, 300, 300)
        self.createCalendar()

    def createCalendar(self):
        vbox = QVBoxLayout()
        calendar = QCalendarWidget()
        calendar.setGridVisible(True) #can be removed only makes the calendar squares visible
        vbox.addWidget(calendar)
        self.setLayout(vbox)

myApp = QApplication(sys.argv)
window = Window()
window.show()




myApp.exec_()
sys.exit(0)