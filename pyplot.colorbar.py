import matplotlib.pyplot as plt
import numpy as np

fig, plots = plt.subplots(nrows=2, ncols=2)

for graphs in plots.flat :
    im = graphs.imshow(np.random.random((4, 2)), vmin=0, vmax=1)

plt.colorbar(im, ax=plots.ravel().tolist())

fig.savefig('pyplot.colorbar.pdf',bbox_inches='tight')
