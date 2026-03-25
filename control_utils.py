# control_utils.py
import numpy as np
import control as ctrl


def make_TransferFunction(numerator, denomerator) -> ctrl.TransferFunction:
    return ctrl.TransferFunction(numerator, denomerator)


# =========================
# Standard Responses
# =========================
def impulse_response(sys, T=None):
    t, y = ctrl.impulse_response(sys, T=T)
    return t, y


def step_response(sys, T=None):
    t, y = ctrl.step_response(sys, T=T)
    return t, y


def forced_response(sys, t, u):
    t, y = ctrl.forced_response(sys, t, u)
    return t, y

# =========================
# System Generators
# =========================
def first_order(k=1, tau=1):
    # H(s) = k / (tau*s + 1)
    return make_TransferFunction([k], [tau, 1])


def second_order(wn=1, zeta=0.5):
    # H(s) = wn^2 / (s^2 + 2*zeta*wn*s + wn^2)
    return make_TransferFunction([wn**2], [1, 2 * zeta * wn, wn**2])


def rlc_series(R, L, C):
    # H(s) = 1 / (LC s^2 + RC s + 1)
    return make_TransferFunction([1], [L * C, R * C, 1])


# =========================
# Filters
# =========================
def low_pass(tau=1):
    return make_TransferFunction([1], [tau, 1])


def high_pass(tau=1):
    return make_TransferFunction([tau, 0], [tau, 1])

# def frequency_response(sys):
#     mag, phase, omega = ctrl.bode(sys, plot=False)
#     return omega, mag, phase
