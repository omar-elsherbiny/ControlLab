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


def plot_grid(items, titles=None, nrows=2, ncols=2, figsize=(12, 8)):
    """
    Plots multiple items in a grid.

    Each item can be:
    - A tuple (t, y) -> time-domain plot
    - A callable f(ax) -> custom plotting function

    Parameters:
    - items: list of items to plot (tuples or callables)
    - titles: optional list of subplot titles (ignored if callable sets its own)
    - nrows, ncols: grid layout
    - figsize: figure size
    """
    n_plots = len(items)
    if titles is None:
        titles = [f"Plot {i+1}" for i in range(n_plots)]

    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)

    # Flatten axes to a 1D array
    if isinstance(axes, np.ndarray):
        axes_list = axes.ravel()
    else:
        axes_list = [axes]

    for i, item in enumerate(items):
        ax = axes_list[i]
        if callable(item):
            # Custom plotting function that accepts ax
            item(ax)
        else:
            # Assume (t, y) tuple
            t, y = item
            ax.plot(t, y)
            ax.set_title(titles[i])
            ax.set_xlabel("Time")
            ax.set_ylabel("Amplitude")
            ax.grid()

    # Hide unused axes
    for ax in axes_list[n_plots:]:
        ax.set_visible(False)

    plt.tight_layout()
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


def plot_pzmap(sys, title="Pole-Zero Map", ax=None):
    """
    Plots the poles and zeros of a system.

    Parameters:
    - sys: control system
    - title: subplot title
    - ax: optional matplotlib Axes object
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

    if ax is None:
        plt.show()


# def plot_bode(sys):
#     import control as ctrl

#     ctrl.bode_plot(sys)
#     plt.show()
