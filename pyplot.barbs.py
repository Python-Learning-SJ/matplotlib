import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-5, 5, 5)
X, Y = np.meshgrid(X, X)
U, V = 12 * X, 12 * Y

data = [(-1.5, .5, -6, -6),
        (1, -1, -46, 46),
        (-3, -1, 11, -11),
        (1, 1.5, 80, 80),
        (0.5, 0.25, 25, 15),
        (-1.5, -0.5, -5, 40)]

fig = plt.figure(figsize = (10,10))

data = np.array(data, dtype=[('x', np.float32),
                             ('y', np.float32),
                             ('u', np.float32),
                             ('v', np.float32)])

plt.barbs(X, Y, U, V)

fig.savefig('pyplot.barbs.pdf',bbox_inches='tight')
