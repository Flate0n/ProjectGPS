from PyQt5 import QtWidgets
import io
import folium
import posn
import Point_in_path
from PyQt5.QtWidgets import QApplication, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *

import sys, random

p1 = posn.sq1
l1 = posn.ln1

# второе окно с картой
class MyApp(QWidget):

    def __init__(self):

        super(MyApp, self).__init__()

        self.setWindowTitle('map')

        self.setMinimumSize(500, 300)

        self.butn=QtWidgets.QPushButton(self)
        self.butn.setText("назад ")
        self.butn.move(0, 0)
        self.butn.adjustSize()


        layout = QVBoxLayout()
        self.setLayout(layout)
        clr =['red','blue','gray','orange','beige','green','darkblue','lightblue','purple','pink','lightgray','black']

        coordinate = l1[-1]
        coordinate2 = (52.257370815151056, 104.26511713595323)
        coordinate3 = (52.25975514950854, 104.26304021817246)
        coordinate0=[coordinate,
                     coordinate2,
                     coordinate3
                    ]
        I=len(coordinate0)
        m = folium.Map(

            zoom_start=16,
            location=coordinate0[0]
        )
        shapesLayer = folium.FeatureGroup(name="warning").add_to(m)
        # маркеры на карте

        for i in range(I) :
            Colr= random.randrange(0, 11)
            n="worker"+str(i+1)
            folium.Marker(location=coordinate0[i], popup=str(n), icon=folium.Icon(color=clr[Colr])).add_to(m)

        poin=Point_in_path.is_point_in_path(coordinate[0],coordinate[1],p1)
        if poin==False:
            color_p1="red"
        else:
            color_p1 = "green"

        folium.Polygon(
            p1,
            weight=2,
            fill_color=color_p1,
            fill_opacity=0.2).add_to(shapesLayer)

        folium.PolyLine(
            l1,
            color="black",
            weight=2
        ).add_to(shapesLayer)


        # сохранение карты
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)
        layout.addWidget(self.butn)

def APP():
    app=QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    APP()



