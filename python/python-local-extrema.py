# Ovaj program mi generira matplotlib figure za graf funkcije f(x) = e^x-x koji koristim u točki 8.1

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - x

x = np.linspace(-7, 3, 400)
y = f(x)

mask = y <= 10
x_plot = x[mask]
y_plot = y[mask]

fig, ax = plt.subplots()

ax.plot(x, y, color = "darkorchid")
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
x_label = -5.9
y_label = 6.1
ax.text(x_label, y_label, r"$f(x) = e^x - x$", fontsize=12, color = "darkorchid")

ax.set_xticks(range(-7, 4))
ax.set_yticks(-2,-1,1,2,3,4,5,6,7,8,9,10)

ax.set_ylim(-2, 10)

fig.savefig("plot.png", bbox_inches="tight", pad_inches=0)

plt.show()

