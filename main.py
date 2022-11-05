# importing various libraries
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QRadioButton, QComboBox, QWidget, QLabel, \
    QLineEdit
from PyQt5.uic.properties import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.animation as anime
import random as randy
import os
import subprocess


FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

Last_cord_x = [50.0]
Last_cord_y = [50.0]


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
        a =1
        self.w = Window()
        self.w.show()


        #self.dialog.show()


# main window
# which inherits QDialog
class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.w = Setup()
        # a figure instance to plot on

        self.figure = plt.figure()
        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        #TODO right layout blah blah blah
        '''        rlayout = QVBoxLayout()
        rlayout.setContentsMargins(1, 1, 1, 1)
        rlayout.addWidget(QLabel("Plot type:"))
        rlayout.addWidget(self.combo)
        rlayout.addWidget(self.table)
        '''
        # 'figure' instance as a parameter to __init__
        #TODO Figure(figsize=(x,y))
        #self.figure = Figure(fig)
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        # Just some buttons
        self.button = QPushButton('show track')
        self.dropdown = QComboBox(self)
        self.dropdown.addItem("Sensor 1")
        self.dropdown.addItem("Sensor 2")
        self.button_config = QPushButton('add config file')
        # Just some radios man
        self.radio = QRadioButton("enable trackers")

        # adding action to the button
        self.button.clicked.connect(self.plot)
        self.button_config.clicked.connect(self.configfile)
        # creating a Vertical Box layout
        layout = QVBoxLayout()
        # adding tool bar to the layout
        layout.addWidget(self.toolbar)
        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout
        layout.addWidget(self.button)

        layout.addWidget(self.button_config)
        layout.addWidget(self.dropdown)
        
        layout.addWidget(self.radio)

        # setting layout to the main window
        self.setLayout(layout)
    # action called by the push button

    def configfile(self):
        path = os.path.normpath('')

        if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])
        elif os.path.isfile(path):
            subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])


    def plot(self):
        # random data
        for i in range(25):
            x = randy.randint(-4, 5)
            y = randy.randint(-4, 5)
            Last_cord_x.append(Last_cord_x[-1] + (x / 2))
            Last_cord_y.append(Last_cord_y[-1] + (y / 2))
        # clearing old figure
            self.figure.clear()
        # create an axis
            ax = self.figure.add_subplot(111)
        # plot data
            ax.plot(Last_cord_x, Last_cord_y, '*-')
        # refresh canvas
            self.canvas.draw()

# driver code
if __name__ == '__main__':
    # creating apyqt5 application
    app = QApplication(sys.argv)
    # creating a window object
    main = Setup()
    # showing the window
    main.show()
    # loop
    sys.exit(app.exec_())
