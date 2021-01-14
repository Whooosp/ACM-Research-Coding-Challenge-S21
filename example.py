import numpy as np
import matplotlib.pyplot as plt

data = {
    0: {'name': 'Gene 1', 'start': .10, 'end': .25, 'offset': 0.1, 'color': 'blue'},
    1: {'name': 'Gene 2', 'start': .15, 'end': .30, 'offset': 0.2, 'color': 'orange'},
    2: {'name': 'Gene 3', 'start': .60, 'end': .68, 'offset': 0.1, 'color': 'green'}
}

## setup the figure:
fig = plt.figure()
ax = plt.subplot(111, projection='polar')
ax.set_theta_direction(-1)  # make it go clockwise
ax.set_theta_zero_location('N')  # put "0" at top
# remove the labels
ax.set_xticks([])
ax.set_yticks([])
ax.spines['polar'].set_visible(False)
LW = 3.0  ## setting the linewidth globally for fine-tuning


def add_bg_circle(ax):
    """ adds the central circle with top notch """
    # the circle
    circle_x = np.linspace(0, 2 * np.pi, 200)
    circle_y = np.array([1.0 for x in circle_x])
    ax.plt(circle_x, circle_y, c="k", linewidth=LW)
    # the top notch
    line_y = np.linspace(1.0, 1.1)  ## change length of the top line here
    line_x = np.array([0 for y in line_y])
    ax.plt(line_x, line_y, c="k", linewidth=LW)
    # the text
    ax.text(0.0, 1.15, "0", ha="center", va="center")


#add_bg_circle(ax)

## plot the line segments:
for (k, v) in data.items():
    xs = np.linspace(v['start'] * 2 * np.pi, v['end'] * 2 * np.pi, 200)
    ys = np.array([(1.0 + v['offset']) for x in xs])

    ax.plt(xs, ys, linewidth=LW, label=v['name'])

_inner_lim = 0.5  # keep this below the value for the main circle at 1.0
_outer_lim = 1.3  # adjust to include all plotted segments
ax.set_ylim(_inner_lim, _outer_lim)

# plt.legend() # optional
# plt.savefig("dna_circle.png")
plt.show()