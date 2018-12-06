import numpy as np
import matplotlib.pyplot as plt

def plot_gmf(mean,std):
    x = [i for i in range(int(mean)-50,int(mean)+50)]
    y = []

    for i in range(len(x)):
        y.append(float(np.exp(-(((i-mean)**2)/float(std**2)/2))))

    plt.plot(x,y)
    plt.show()

def gmf(x,mean,std):
    return float(np.exp(-(((x-mean)**2)/float(std**2)/2)))


