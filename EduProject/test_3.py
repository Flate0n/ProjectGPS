from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from test_2 import Window
from test_4 import MyApp


app=QtWidgets.QApplication(sys.argv)
Mwindow=Window()
Mwindow.show()

def map():
    global window
    window = MyApp()
    Mwindow.close()
    window.show()

    def clsmap():
        Mwindow.show()
        window.close()

    window.butn.clicked.connect(clsmap)

Mwindow.btn2.clicked.connect(map)


sys.exit(app.exec_())

