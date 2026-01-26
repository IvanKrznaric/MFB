# ovaj program mi generira matplotlib figure za graf funkcije f(x) = x^2/(4-x) koji koristim u točki 8.2

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2/(4-x)

# Left side of the asymptote
x_left = np.linspace(-25, 3.999, 2000)
y_left = f(x_left)

# Right side of the asymptote
x_right = np.linspace(4.001, 25, 2000)
y_right = f(x_right)


fig, ax = plt.subplots()

ax.plot(x_left, y_left, color = "darkorchid")
ax.plot(x_right, y_right, color = "darkorchid")
ax.grid(True)
ax.set_facecolor("lavenderblush")  # light gray


# Remove the box frame
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Move axes to the origin
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Show ticks only on x and y axes
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Add the formula near the curve
# Choose a point on the curve where the label will be readable
x_label = -20
y_label = 17
ax.text(x_label, y_label, r"$f(x) = \frac{x^2}{4-x}$", fontsize=16, color = "darkorchid")

ax.set_xticks(range(-25, 26,5))
ax.set_yticks(range(-50,50,10))

ax.set_ylim(-50, 50)

fig.savefig("IntMon.png", bbox_inches="tight", pad_inches=0)

plt.show()

