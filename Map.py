import os
import numpy as np
import matplotlib.pyplot as plot
from parse import parse, get_source

features = parse("Genome.gb")
source = get_source("Genome.gb")

data = {}
startPoint = 0

for feature in features:
    entry = {'name': feature.qualifiers.get('gene')[0], 'start': feature.location.start.position,
             'end': feature.location.end.position, 'color': 'red'}
    print(entry['start'] + 2)
    # print(len(feature))
    # print(feature.location)
    # print(feature.location.start.position)
    data.update({startPoint: entry})
    startPoint += 1
    # if startPoint == 2:
    #     break

print(data)
print()
print(source)
print(len(source))

fig = plot.figure()
ax = plot.subplot(111, projection='polar')
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
r = np.arange(0, 1, 0.001)
theta = 2 * 2 * np.pi * r

ind = 800
thisr, thistheta = r[ind], theta[ind]
lastend = 0
previousoffset = False

for (k, v) in data.items():
    offset = .01001 if v['start'] < lastend and previousoffset else .01
    previousoffset = offset == .01
    print(v['start'])
    print(lastend)
    # print(offset)
    xs = np.linspace(v['start'] * 2 * np.pi / (len(source)), v['end'] * 2 * np.pi / len(source), 200)
    lastend = v['end']
    dist = 200+offset
    ys = np.array([(dist) for x in xs])
    ax.plot(xs, ys, linewidth=3, label=v['name'])

ax.annotate('annotation',
            xy=(0, 1),
            # xytext=(.05, .8),
            # textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=.08),
            horizontalalignment='left',
            verticalalignment='bottom')
ax.set_xticks([])
ax.set_yticks([])
ax.spines['polar'].set_visible(False)
plot.show()
