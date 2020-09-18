# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def plotSpectrum(filename):
    channel_list = []
    count_list = []
    fr = open(filename, "r")
    while True:
        line = fr.readline()
        if not line:
            break
        spl = line.split()
        channel_list.append(int(spl[0]))
        count_list.append(int(spl[1]))
    channel_np = np.array(channel_list)
    count_np = np.array(count_list)

    plt.plot(channel_np, count_np, "r-")
    plt.show()

    fr.close()
