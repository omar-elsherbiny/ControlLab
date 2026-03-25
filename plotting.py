# plotting.py
import matplotlib.pyplot as plt
import control as ctrl
import numpy as np

def plot_time(t, y, title="Response"):
    plt.figure()
    plt.plot(t, y)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()


def plot_compare(t, signals, labels, title="Comparison"):
    plt.figure()
    for y, label in zip(signals, labels):
        plt.plot(t, y, label=label)

    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.show()

def plot_pzmap(sys, title="Pole-Zero Map"):
    plt.figure()
    poles = ctrl.poles(sys)
    zeros = ctrl.zeros(sys)

    plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Poles', s=100)
    plt.scatter(np.real(zeros), np.imag(zeros), marker='o', facecolors='none', edgecolors='b', label='Zeros', s=100)
    plt.axhline(0, color='k', linewidth=0.5)
    plt.axvline(0, color='k', linewidth=0.5)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


# def plot_bode(sys):
#     import control as ctrl

#     ctrl.bode_plot(sys)
#     plt.show()
