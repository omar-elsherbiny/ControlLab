# plotting.py
import matplotlib.pyplot as plt
import control as ctrl
import numpy as np


def plot_time(t, y, title="Response", ax=None) -> None:
    if ax is None:
        plt.figure()
        ax = plt.gca()
    ax.plot(t, y)
    ax.set_title(title)
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.grid()


def plot_compare(t, signals, labels, title="Comparison", ax=None) -> None:
    """
    Plots multiple signals on the same axes.

    Parameters:
    - t: time vector
    - signals: list of y arrays
    - labels: list of labels for each signal
    - title: plot title
    - ax: optional matplotlib Axes object
    """
    if ax is None:
        plt.figure()
        ax = plt.gca()

    for y, label in zip(signals, labels):
        ax.plot(t, y, label=label)

    ax.set_title(title)
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.legend()
    ax.grid()

    # Only show if figure was created here
    if ax is plt.gca():
        plt.show()


def plot_grid(items, nrows=2, ncols=2, figsize=(12, 10)) -> None:
    """
    Simple grid plot for time series or custom Axes callables.

    Parameters:
    - items: list of (t, y) tuples or callables(ax)
    - nrows, ncols: grid layout
    - figsize: figure size
    """
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    axes = np.array(axes).flatten()

    for i, item in enumerate(items):
        ax = axes[i]
        if callable(item):
            item(ax)
        else:
            t, y, *title = item
            ax.plot(t, y)
            ax.set_title(title[0] if title else "")
            ax.set_xlabel("Time")
            ax.set_ylabel("Amplitude")
            ax.grid()

    for ax in axes[len(items):]:
        ax.set_visible(False)

    plt.tight_layout()
    plt.show()


def plot_pzmap(
    sys, title="Pole-Zero Map", ax=None, xlim=(-10, 1), ylim=(-10, 10)
) -> None:
    """
    Plots the poles and zeros of a system.

    Parameters:
    - sys: control system
    - title: subplot title
    - ax: optional matplotlib Axes object
    - xlim: tuple (xmin, xmax) to zoom x-axis
    - ylim: tuple (ymin, ymax) to zoom y-axis
    """
    if ax is None:
        fig, ax = plt.subplots()

    poles = ctrl.poles(sys)
    zeros = ctrl.zeros(sys)

    ax.scatter(
        np.real(poles), np.imag(poles), marker="x", color="r", label="Poles", s=100
    )
    ax.scatter(
        np.real(zeros),
        np.imag(zeros),
        marker="o",
        facecolors="none",
        edgecolors="b",
        label="Zeros",
        s=100,
    )
    ax.axhline(0, color="k", linewidth=0.5)
    ax.axvline(0, color="k", linewidth=0.5)
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    if ax is None:
        plt.show()


# def plot_bode(sys):
#     import control as ctrl

#     ctrl.bode_plot(sys)
#     plt.show()
