# %%
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-whitegrid")
plt.rcParams.update({
    'figure.figsize': (12, 5)
})

# %%

# Damped Harmonic Oscillator Parameters
zeta = 0.9
wn = 0.2


def reference_signal(x, uc, t):
    y1 = x[0]
    y2 = x[1]

    y1_dot = y2
    y2_dot = -wn**2*y1 - 2*zeta*wn*y2 + wn**2*uc
    return np.array([y1_dot, y2_dot])


dt = 0.1
t = np.arange(0, 50+dt, dt)

u_c = np.ones(len(t))
u_c[0:len(t)//4] = 0

x = np.zeros((2, len(t)))
x[:, 0] = np.array([0, 0])
for i in range(1, len(t)):
    x[:, i] = x[:, i-1] + dt*reference_signal(x[:, i-1], u_c[i], t[i])

r = x[0, :]
v = x[1, :]

fig, ax = plt.subplots(2, 1)
ax[0].plot(t, r, label="$r(t)$")
ax[0].legend()
ax[1].plot(t, v, label=r"$\dot{r}(t)$")
plt.legend()
plt.show()

# %%
