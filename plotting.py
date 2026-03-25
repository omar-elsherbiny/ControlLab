# plotting.py
import matplotlib.pyplot as plt


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


# def plot_bode(sys):
#     import control as ctrl

#     ctrl.bode_plot(sys)
#     plt.show()
