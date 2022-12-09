# importing various libraries
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QRadioButton, QComboBox, QWidget, QLabel, \
    QLineEdit
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.animation as anime
import random as randy
import os
import server

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

Last_cord_x = [50.0]
Last_cord_y = [50.0]

import socket
import threading
import time
import pickle
import numpy
import matplotlib.pyplot as plt
from multiprocessing import Process

'''
class Setup(QDialog):
    def __init__(self, parent=None):
        super(Setup, self).__init__(parent)
        self.title = "setup Page"
        self.buttonvon = QPushButton('Continue')
        self.dropdown = QComboBox(self)
        self.dropdown.addItem("N")
        self.dropdown.addItem("E")
        self.dropdown.addItem("S")
        self.dropdown.addItem("W")
        self.textbox = QLineEdit(self)
        self.label2 = QLabel("Sensor 1 Orientation")
        self.label = QLabel("Sensor 2 Orientation")
        self.dropdown2 = QComboBox(self)
        self.dropdown2.addItem("N")
        self.dropdown2.addItem("E")
        self.dropdown2.addItem("S")
        self.dropdown2.addItem("W")

        self.buttonvon.clicked.connect(self.on_click)
        self.setGeometry(10, 10, 800, 480)

        layout = QVBoxLayout()
        layout.addWidget(self.textbox)
        layout.addWidget(self.buttonvon)
        layout.addWidget(self.label2)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.label)
        layout.addWidget(self.dropdown2)

        self.setLayout(layout)

    def on_click(self):
        a = 1
        self.w = Window()
        self.w.show()

        # self.dialog.show()
'''

# main window
# which inherits QDialog
class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        #self.w = Setup()
        #todo check this out ^
        # a figure instance to plot on

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setXRange(0, 9, padding=0)
        self.graphWidget.setYRange(0, 6, padding=0)

        self.pen1 = pg.mkPen(color=(255, 0,0), width=2)
        self.pen2 = pg.mkPen(color=(0, 255,0), width=2)
        self.pen3 = pg.mkPen(color=(255, 0, 255), width=2)
        self.pen4 = pg.mkPen(color=(0, 255, 255), width=2)

        self.x = [1]
        self.y = [1]

        t1 = threading.Thread(target=server.startserver)
        t1.start()


        layout = QVBoxLayout()

        self.setLayout(layout)

        layout.addWidget(self.graphWidget)

        self.date_line1 = self.graphWidget.plot()
        self.date_line2 = self.graphWidget.plot()
        self.date_line3 = self.graphWidget.plot()

        x = True

        while x:
            x = server.sufficient_data()
            if x == False:
                break
            y = server.sufficient_data2()
            if y == False:
                break

        self.timer = QTimer()
        self.timer.setInterval(5)

        self.timer.timeout.connect(self.update_stuff)

        self.timer.start()

    def update_stuff(self):

        x, y, x2, y2 = server.BIGDATA()
        x2_1, y2_1, x2_2, y2_2 = server.BIGDATA2()
        fakerx = [-3, -2]
        fakery = [-3, -2]

        a = x2_1  # [-9:-1]
        b = y2_1  # [-9:-1]
        two_sensors = False

        if x[-1] > 2 and x2_1[-1] < 5.5:
            two_sensors = True
            a = x[-9:-1]
            b = x2_1[-9:-1]
            c = y[-9:-1]
            d = y2_1[-9:-1]
            #print(len(a), len(b))
            totalx = 0
            totaly = 0
            for i in range(8):
                temp = b[i] - a[i]
                totalx += temp
                temp = d[i] - c[i]
                totaly += temp

            avg1 = round(totalx/8, 2)
            avg2 = round(totaly/8, 2)
            new_listx = []
            new_listy = []
            for i in range(8):
                new_listx.append(b[i]-avg1)
                new_listy.append(d[i]-avg2)

            self.date_line1.clear()
            self.date_line2.clear()
            self.date_line3.setData(new_listx[-9:-1], new_listy[-9:-1], pen=self.pen2)






        else:
            self.date_line3.clear()
            self.date_line1.setData(x[-8:-1], y[-8:-1], pen=self.pen2)
            self.date_line2.setData(x2_1[-8:-1], y2_1[-8:-1], pen=self.pen2)

        #print(x[-9:-1])





    # action called by the push button



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # creating a window object
    main = Window()
    # showing the window
    main.show()
    # loop
    sys.exit(app.exec_())
