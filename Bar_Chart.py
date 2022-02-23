import numpy as numpy
import matplotlib.pyplot as plt

# Creating the dateset
data = {'SJ':10, 'SS':5, 'GL':2, 'EH':12}
family = list(data.keys())
month = list(data.values())

fig = plt.figure(figsize = (10,5))

# Creating the bar plot
plt.bar(family,month, color ='green', width = 0.5)

plt.xlabel("No of family")
plt.ylabel("Months")
plt.title("Family members birthday month")
fig.savefig('Bar_chart.pdf',bbox_inches='tight')
