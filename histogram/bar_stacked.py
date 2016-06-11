#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
N = len(array)
count = [8, 11, 14, 11, 6, 11, 10, 11, 6, 8]
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence


#p1 = plt.bar(ind, menMeans, width, color='r', yerr=menStd)
p1 = plt.bar(ind, count, width, color='r')

plt.ylabel('Count')
plt.title('Count by integer')
plt.xticks(ind + width/2., array)
plt.yticks(np.arange(0, max(count)+10, 10))
plt.legend((p1[0], None), ('Men', None))

plt.show()
