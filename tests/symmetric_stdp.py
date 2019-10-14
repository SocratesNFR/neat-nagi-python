import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from nagi.constants import SYMMETRIC_HEBBIAN_PARAMS, SYMMETRIC_ANTI_HEBBIAN_PARAMS
from nagi.stdp import *


def plot_symmetric_hebbian():
    p = SYMMETRIC_HEBBIAN_PARAMS

    x = [i for i in range(-50, 51)]
    y = [symmetric_hebbian(dt, p['a'], p['std']) for dt in range(-50, 51)]

    fig = plt.figure()
    plt.ylabel("delta_w")
    plt.xlabel("delta_t (in ms)")
    plt.grid()
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.plot(x, y, "r-")
    plt.title("symmetric_hebbian")
    plt.show()


def plot_symmetric_anti_hebbian():
    p = SYMMETRIC_ANTI_HEBBIAN_PARAMS

    x = [i for i in range(-50, 51)]
    y = [symmetric_anti_hebbian(dt, p['a'], p['mean'], p['std']) for dt in range(-50, 51)]

    fig = plt.figure()
    plt.ylabel("delta_w")
    plt.xlabel("delta_t (in ms)")
    plt.grid()
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.plot(x, y, "r-")
    plt.title("symmetric_hebbian")
    plt.show()


if __name__ == '__main__':
    plot_symmetric_hebbian()
    plot_symmetric_anti_hebbian()
