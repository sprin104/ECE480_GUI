import matplotlib.pyplot as plt
import matplotlib.animation as anime
import random as randy
import time
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(111)

Last_cord_x = [50.0]
Last_cord_y = [50.0]

Counter = 0


def animation(i):


    y_temp = randy.randrange(-4, 5)
    x_temp = randy.randrange(-4, 5)
    Last_cord_x.append(Last_cord_x[-1] + (x_temp/2))
    Last_cord_y.append(Last_cord_y[-1] + (y_temp/2))
    ax1.set_facecolor('#18453b')

    if len(Last_cord_x) > 20:
        plt.plot(Last_cord_x[-21:-19], Last_cord_y[-21:-19], color='#18453b', linestyle='solid', linewidth=3)

        #ax1.clear()

    plt.xlim(0, 100)
    plt.ylim(0, 100)

    return plt.plot(Last_cord_x[-3:-1], Last_cord_y[-3:-1],color='white', linestyle='solid', linewidth=2)

ani = anime.FuncAnimation(fig, animation, interval=0)
plt.show()
