# ovaj program mi generira matplotlib figure za graf funkcije f(x) = x^3-4x koji koristim u točki 8.3

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3-4*x

x = np.linspace(-5, 5, 400)
y = f(x)

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
x_label = 2.5
y_label = 2.5
ax.text(x_label, y_label, r"$f(x) = x^3-4x$", fontsize=16, color = "darkorchid")

ax.set_xticks(range(-5, 5))
yticks = [-5,-4,-3,-2,-1,1,2,3,4,5]
ax.set_yticks(yticks)

ax.set_ylim(-5, 5)

fig.savefig("Conv.png", bbox_inches="tight", pad_inches=0)

plt.show()

