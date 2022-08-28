import numpy as np
import matplotlib.pyplot as plt

samp1 = np.random.normal(loc=0., scale=1., size=100)
samp2 = np.random.normal(loc=1., scale=2., size=100)
samp3 = np.random.normal(loc=0.3, scale=1.2, size=100)
f, ax = plt.subplots(1, 1, figsize=(5,4))
c = "red"
b = "blue"
ax.boxplot((samp1, samp2, samp3), notch=True, patch_artist=True,
            boxprops=dict(facecolor=c, color=b),
            capprops=dict(color=c),
            whiskerprops=dict(color=b),
            flierprops=dict(color=c, markeredgecolor=c),
            medianprops=dict(color=b))
ax.set_xticklabels(['sample 1', 'sample 2', 'sample 3'])
plt.tight_layout()
plt.show()
plt.savefig('boxplot.pdf')