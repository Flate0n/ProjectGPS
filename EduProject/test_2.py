from PyQt5 import QtWidgets
import io
import folium
from PyQt5.QtWidgets import QApplication, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *

import sys, random

def ran():
    S = random.randrange(5, 40)
    return S
# основное окно
class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()


        self.setWindowTitle("test programm")
        self.setGeometry(300, 300, 400, 160)


        #температура
        self.txt_temp = QtWidgets.QLabel(self)
        self.txt_temp.setText("Температура :")
        self.txt_temp.move(10, 17)
        self.txt_temp.adjustSize()
        self.temp_txt = QtWidgets.QLineEdit(self)
        self.temp_txt.move(85, 15)
        self.temp_txt.adjustSize()

        #давление
        self.txt_pres = QtWidgets.QLabel(self)
        self.txt_pres.setText("Давление :")
        self.txt_pres.move(25, 38)
        self.txt_pres.adjustSize()
        self.pres_txt=QtWidgets.QLineEdit(self)
        self.pres_txt.move(85, 35)
        self.pres_txt.adjustSize()

        #кнопка 1
        self.btn=QtWidgets.QPushButton(self)
        self.btn.setText("Обновить данные ")
        self.btn.move(60, 70)
        self.btn.adjustSize()
        # кнопка 2
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText("найти на карте")
        self.btn2.move(230, 38)
        self.btn2.adjustSize()

        self.push_btn()
        self.push_btn2()
        self.worker()
        self.wrt()

    def wrt(self):
        #обнавление данных
        self.temp_txt.setText(str(ran()))
        self.pres_txt.setText(str(ran()*11))


    def worker(self):
        geek_list = ["worker_1", "worker_2", "worker_3"]
        self.wrks = QComboBox(self)
        self.wrks.setGeometry(230, 15, 120, 20)
        self.wrks.addItems(geek_list)

    def find(self):
        index = self.wrks.currentIndex()
        print("Index : " + str(index))
        return index

    def push_btn(self):
        # обработка нажатия кнопки
        self.btn.clicked.connect(self.wrt)
        self.btn.clicked.connect(self.find)

    def push_btn2(self):
        # обработка нажатия второй кнопки
        self.btn2.clicked.connect(self.find)

