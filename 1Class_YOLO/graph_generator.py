# create charts for mean
import numpy as np
import matplotlib.pyplot as plt


N = 15
true_positive = (7)
false_positive = (6)
# menStd = (2, 3, 4, 1, 2)
# womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, true_positive, width)
p2 = plt.bar(ind, false_positive, width,
             bottom=true_positive)

plt.ylabel('Number of images tested')
plt.title('Average Precision for 1 Class (Weights = 1000)')
plt.xticks(ind, ('Snapple'), rotation='vertical')
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('True Positive', 'False Positive'))

# plt.show()
plt.tight_layout()
plt.savefig('AP1000.svg')

plt.show()
