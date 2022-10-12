import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
years = ['Accuracy', 'Precision', 'Recall', 'F1-score']
values = [0.96, 0.89, 0.89, 0.89]
colors = ['black', 'gray', 'silver', 'whitesmoke']

plt.bar(x, values, width=0.6, color=colors)
plt.xticks(x, years)

plt.tick_params(axis='x', labelsize=18)
plt.tick_params(axis='y', labelsize=20)


plt.show()