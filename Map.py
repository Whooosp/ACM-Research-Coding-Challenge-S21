import os
import matplotlib.transforms
import numpy as np
import matplotlib.pyplot as plt
from parse import parse, get_source, get_locus

features = parse("Genome.gb")
source = get_source("Genome.gb")
locus = get_locus("Genome.gb")


data = {}
startPoint = 0

for feature in features:
    entry = {'name': (feature.qualifiers.get('gene')[0] + ' (' + feature.qualifiers.get('product')[0] + ')'),
             'start': feature.location.start.position,
             'end': feature.location.end.position, 'dir': feature.strand}
    data.update({startPoint: entry})
    startPoint += 1

fig = plt.figure()
ax = plt.subplot(111, projection='polar')
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
r = np.arange(0, 1, 0.001)
theta = 2 * 2 * np.pi * r


lastend = 0
previousoffset = False

for (k, v) in data.items():
    offset = .1 if v['start'] < lastend and not previousoffset else 0
    previousoffset = offset == .1
    # print(v['start'])
    # print(lastend)
    # print(offset)
    # print(v['start'] * 2 * np.pi / (len(source)))
    xs = np.linspace(v['start'] * 2 * np.pi / (len(source)), v['end'] * 2 * np.pi / len(source), 200)
    lastend = v['end']
    dist = 1.0 + offset
    ys = np.array([(dist) for x in xs])
    p = ax.plot(xs, ys, linewidth=3, label=v['name'])
    #print(v['dir'])
    # if the gene is read on the normal strand, make a green clockwise arrow
    # else if the gene is read on the complementary strand (and therefore in reverse)
    # make a red counter-clockwise arrow
    if v['dir'] > 0:
        ax.arrow(xs[100], ys[100], xs[105] - xs[100], ys[105] - ys[100], fc='g', ec='g', head_width=.1, head_length=.1)
    else:
        ax.arrow(xs[100], ys[100], xs[100] - xs[105], ys[100] - ys[105], fc='r', ec='r', head_width=.1, head_length=.1)

ax.set_xticks([])
ax.set_yticks([0, 1], minor=False)
ax.set_yticklabels(('', '$source$'))
labeloffset = matplotlib.transforms.ScaledTranslation(-.9, .2, fig.dpi_scale_trans)
for label in ax.yaxis.get_majorticklabels():
    label.set_transform(label.get_transform() + labeloffset)

ax.legend(loc='lower left', bbox_to_anchor=(-.4, -.1))
ax.spines['polar'].set_visible(False)
plt.title(source.qualifiers.get('organism')[0], loc='center', pad=10)
plt.savefig(locus + '.jpeg')
plt.close()
exit(0)
