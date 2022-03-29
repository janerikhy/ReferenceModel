import numpy as np


def z1(x1, xd):
    return x1 - xd


def z2(x2, alpha1):
    return x2 - alpha1


def z1_dot(x2, x_d_dot):
    return x2 - x_d_dot


def alpha1(xd_dot, k1, z1):
    return xd_dot - k1*z1


def alpha1_dot(x_d_dot, x_d_2dot, k1, z2, alpha):
    return x_d_2dot - k1*(z2+alpha - x_d_dot)


def tau(z_1, alpha1, alpha1_dot, d, m, k2, z_2):
    return m*(-z_1 + alpha1_dot + d/m*alpha1 - k2*z_2)


def controller(x1, x2, xd, xd_dot, xd_dotdot, k1, k2, d, m):
    z_1 = z1(x1, xd)
    alpha = alpha1(xd_dot, k1, z_1)
    z_2 = z2(x2, alpha)
    #z_1_dot = z1_dot(x2, xd_dot)
    alpha_dot = alpha1_dot(xd_dot, xd_dotdot, k1, z_2, alpha)
    control = tau(z_1, alpha, alpha_dot, d, m, k2, z_2)
    return control
