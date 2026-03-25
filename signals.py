# signals.py
import numpy as np


def time_vector(t_end=10, n=1000):
    return np.linspace(0, t_end, n)


def unit_step(t):
    return np.ones_like(t)


def unit_impulse(t, eps=1e-3):
    u = np.zeros_like(t)
    u[0] = 1 / eps
    return u


def ramp(t):
    return t


def parabola(t):
    return 0.5*t**2


def sinusoid(t, freq=1):
    return np.sin(2 * np.pi * freq * t)


def square_wave(t, freq=1):
    return np.sign(np.sin(2 * np.pi * freq * t))
