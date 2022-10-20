# importing various libraries
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QRadioButton, QComboBox
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
# main window
# which inherits QDialog
class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # a figure instance to plot on

        self.figure = plt.figure()
        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        #TODO look at below \/
        '''
        rightlayout blah blah blah
        rlayout = QVBoxLayout()
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
        self.radio = QRadioButton("enable trakers")

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
        layout.move(1000, 32)
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
    main = Window()
    # showing the window
    main.show()
    # loop
    sys.exit(app.exec_())
