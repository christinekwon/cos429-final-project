# create charts for mean 
import numpy as np
import matplotlib.pyplot as plt


N = 15
true_positive = (16,10,17,19,6,3,3,8,13,2,2,5,10,4,13)
false_positive = (13,4,41,26,8,8,4,5,3,9,5,5,2,0,10)
# menStd = (2, 3, 4, 1, 2)
# womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, true_positive, width)
p2 = plt.bar(ind, false_positive, width,
             bottom=true_positive)

plt.ylabel('Number of images tested')
plt.title('Average Precision Per Class (Weights = 1000)')
plt.xticks(ind, ('CheezIts', 'Dannon Yogurt', 'Eggs', 'Honest Tea', 'Milk', 'Miss Vickies', 'Oikos Yogurt', 'Powerade', 'Pringles', 'Kozyshack Pudding', 'Silk', 'Snapple', 'Stacy\'s Pita Chips', 'Open Water', 'Tropicana Probiotics'), rotation='vertical')
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('True Positive', 'False Positive'))

# plt.show()
plt.tight_layout()
plt.savefig('AP1000.svg')

plt.show()
