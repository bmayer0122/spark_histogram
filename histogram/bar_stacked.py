#!/usr/bin/env python
# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt
import sys
from ast import literal_eval as make_tuple

f = open('histogram.txt')
line = f.readline()
tup = make_tuple(line)
index = tup[0]
count = tup[1]

N = len(index)-1
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence


tickSize = max(count)/10
#p1 = plt.bar(ind, menMeans, width, color='r', yerr=menStd)
p1 = plt.bar(ind, count, width, color='r')

plt.ylabel('Count')
plt.title('Count by integer')
plt.xticks(ind + width/2., index)
plt.yticks(np.arange(0, max(count)+tickSize, tickSize))
plt.legend((p1[0], None), ('Count', None))

plt.show()
