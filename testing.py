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
import subprocess
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


# main window
# which inherits QDialog
class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.w = Setup()
        # a figure instance to plot on

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setXRange(0, 11)
        self.graphWidget.setYRange(0, 6)

        self.pen1 = pg.mkPen(color=(255, 0,0), width=2)
        self.pen2 = pg.mkPen(color=(0, 255,0), width=2)

        self.x = [1]
        self.y = [1]

        t1 = threading.Thread(target=server.startserver)
        t1.start()


        layout = QVBoxLayout()

        self.setLayout(layout)

        layout.addWidget(self.graphWidget)

        self.date_line1 = self.graphWidget.plot()
        self.date_line2 = self.graphWidget.plot()

        x = True

        while x:
            x = server.sufficient_data()

        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_stuff)

        self.timer.start()

    def update_stuff(self):

        x, y, x2, y2 = server.BIGDATA()
        x1, y1, x2_2, y2_2 = server.BIGDATA2()

        if len(x1) >= 10:
            self.date_line1.setData(x1[-9:-1], y1[-9:-1], pen=self.pen1)

        if len(x) >= 10:
            self.date_line1.setData(x[-9:-1], y[-9:-1], pen=self.pen1)

        if len(x2) >= 20:
            #TODO chage back to 10
            self.date_line2.setData(x2[-9:-1], y2[-9:-1], pen=self.pen2)
    # action called by the push button



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # creating a window object
    main = Setup()
    # showing the window
    main.show()
    # loop
    sys.exit(app.exec_())
