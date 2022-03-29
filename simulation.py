# %%
from referenceModel import dt, t, r, v, a, dir
from backstepping import controller
from observer import observer
import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use('seaborn-whitegrid')
plt.rcParams.update({
    'figure.figsize': (12, 4)
})

m = 10
g = 9.81
d = 1.4


def dxdt(x, u):
    return np.array([x[1], -d/m*x[1] + u/m])


k1 = 8
k2 = 5

x = np.zeros((2, len(t)))
x_hat = np.zeros((3, len(t)))

x[:, 0] = np.array([0.0, 0.])
x_hat[:, 0] = np.array([0.4, 0, .5])

tau = 0
for i in range(1, len(t)):
    x[:, i] = x[:, i-1] + dt*dxdt(x[:, i-1], tau)
    tau = controller(x[0, i], x[1, i], r[i], v[i], a[i], k1, k2, d, m)
    x_hat[:, i] = x_hat[:, i-1] + dt*observer(x_hat[:, i-1], x[0, i], tau)


fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(t, x[0, :], label="$x$")
ax[0].set_ylabel("Position $[m]$")
ax[0].legend()
ax[1].plot(t, x[1, :], label="$v$")
ax[1].set_ylabel("Velocity $[m/s]$")
ax[1].set_xlabel("$t \; [s]$")
ax[1].legend()
plt.show()


fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(t, x[0, :], label="$x$")
ax[0].plot(t, r[:], label="$x_d$")
ax[0].legend()
ax[1].plot(t, x[1, :], label="$v$")
ax[1].plot(t, v[:], label="$v_d$")
ax[1].legend()
plt.savefig(os.path.join(dir, 'simulation_w_backstepping.png'), dpi=350)
plt.show()

fig, ax = plt.subplots(3, 1, sharex=True)
ax[0].set_title("Observer")
ax[0].plot(t, x_hat[0, :], label=r"$\hat{x}$")
ax[0].legend()
ax[1].plot(t, x_hat[1, :], label=r"$\hat{v}$")
ax[1].legend()
ax[2].plot(t, x_hat[2, :], label=r"$\hat{b}$")
ax[2].legend()
plt.savefig(os.path.join(dir, 'ObserverResults.png'), dpi=350)
plt.show()

# %%
