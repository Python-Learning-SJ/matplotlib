# Implementation of matplotlib.pyplot.acorr()
# function

import matplotlib.pyplot as plt
import numpy as np

# Time series data
geeks = np.array([24.40, 110.25, 20.06, 22.00, 61.90,
                  7.80, 15.00, 22.80, 34.90, 57.30])

fig = plt.figure(figsize = (10,10))

# Plot autocorrelation
plt.acorr(geeks, maxlags = 9)

# Add labels to autocorrelation plot
plt.title("Autocorrelation of Geeksforgeeks Users data")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

#Display the autocorrelation
fig.savefig('acorr_function.pdf',bbox_inches='tight')
