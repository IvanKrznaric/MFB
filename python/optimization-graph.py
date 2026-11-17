import numpy as np
import matplotlib.pyplot as plt

# xvals
x = np.linspace(-3,3,250)

# y = f(x)
y = 2*x**3 - 6*x

colors = ['m', 'g', 'r', 'b']

# duljina koordinatnih osi i razmak između oznaka
xmin, xmax, ymin, ymax = -3, 2, -5, 5
ticks_frequency = 1

# Plot koordinatnog sustava i grafa
fig, ax = plt.subplots(figsize=(15,5))
plt.plot(x,y)


# skaliranje koordinatnih osi
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='auto')

# koordinatne osi
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# oznake koordinatnih osi
ax.set_xlabel('x', size=14, labelpad=-24, x=1.1,)
ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

# postavljanje oznaka koordinata
x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])


# koordinatna mreža
ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

# strelice na krajevima koordinatnih osi
arrow_fmt = dict(markersize=4, color='black', clip_on=False)
ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

#spremanje plota
fig.savefig("optimization-graph.png", bbox_inches="tight", pad_inches=0.5)

plt.show()
