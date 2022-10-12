# summarize the data
# Load libraries
from pandas import read_csv
import matplotlib.pyplot as plt

...

# Load dataset
url = "C:/Users/dugun/scatter.csv"
names = ['X', 'Y', 'class']
dataset = read_csv(url, names=names)

cat_markers = [['Probe', 'o', 'black'], ['Irrelevant', '^', 'gray']]

for cat, marker, color in cat_markers:
    df_cat = dataset[dataset['class'] == cat]
    plt.scatter(data = df_cat, x = 'X', y = 'Y', marker = marker, c=color)

plt.ylabel('Standardized P300 Amplitude', fontdict={'size': 16})

ax = plt.gca()
ax.axes.xaxis.set_visible(False)


plt.legend(['Probe','Irrelevant'], loc=(0.75, 0.85))

plt.show()


