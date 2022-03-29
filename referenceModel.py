import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-whitegrid")
plt.rcParams.update({
    'figure.figsize': (12, 5)
})


# Damped Harmonic Oscillator Parameters
zeta = 0.9
wn = 0.2


def reference_signal(x, uc, t):
    # Simle reference model generated by harmonic oscillator
    y1 = x[0]
    y2 = x[1]

    y1_dot = y2
    y2_dot = -wn**2*y1 - 2*zeta*wn*y2 + wn**2*uc
    return np.array([y1_dot, y2_dot])


dt = 0.1
t = np.arange(0, 50+dt, dt)

# The reference positions
u_c = np.ones(len(t))
u_c[0:len(t)//4] = 0

# State vector
x = np.zeros((2, len(t)))
x[:, 0] = np.array([0, 0])

# Derive the time soluion using simple forward euler
for i in range(1, len(t)):
    x[:, i] = x[:, i-1] + dt*reference_signal(x[:, i-1], u_c[i], t[i])


# Reference position r
r = x[0, :]

# Reference velocity v
v = x[1, :]


fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(t, r, label="$r(t)$")
ax[0].set_ylabel("$Position \; [m]$")
ax[0].legend()
ax[1].plot(t, v, 'g-', label=r"$\dot{r}(t)$")
ax[1].set_ylabel("$Velocity \;\; [m/s]$")
ax[1].set_xlabel("$t \; [s]$")
ax[1].legend(loc="upper left")
plt.savefig('reference_pos_vel.png', dpi=350)
plt.show()
