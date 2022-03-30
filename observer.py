import numpy as np

# Set the observer parameters
m_obs = .4       # 1 kg difference from simulation model
d_obs = 1       # .4 difference from simulation model

# Observer gains
L1 = 1
L2 = 3
L3 = .6


def observer(x, y, tau):
    x1 = x[0]
    x2 = x[1]
    b = x[2]    # Bias
    x_bar = y - x1
    x1_hat = x2 + L1*x_bar
    x2_hat = 1/m_obs*(-d_obs*x2 + tau + b + L2*x_bar)
    b_hat = L3*x_bar
    return np.array([x1_hat, x2_hat, b_hat])


if __name__ == "__main__":
    print(__file__)
