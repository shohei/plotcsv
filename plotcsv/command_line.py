from matplotlib import pyplot as plt
import numpy as np

def do_plot(filename):
    data = np.genfromtxt(filename, delimiter=',',names=['x', 'y'])
    plt.plot(data['x'],data['y'],color='r')
    plt.show()

if __name__=="__main__":
    do_plot()
