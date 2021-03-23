from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber
from PySide2.QtCore import QTime, QTimer, SIGNAL, QLocale
import sys


class DigitalClock(QLCDNumber):
    def __init__(self):
        super(DigitalClock, self).__init__()
        self.resize(500,200)
        timer = QTimer(self)
        self.connect(timer, SIGNAL('timeout()'), self.showTime)
        timer.start(1000)
        self.showTime()
        self.setStyleSheet("background-color: black")
        self.setStyleSheet("background-color: red")

    def showTime(self):
        time = QTime.currentTime()
        locale  = QLocale(QLocale.English, QLocale.UnitedStates)
        text = locale.toString(time, "hh:mm")
        if (time.second() % 2) == 0:
            text = text[:2] + " " + text[3:]
        self.display(text)


myApp = QApplication(sys.argv)
window = DigitalClock()
window.show()

myApp.exec_()
sys.exit(0)