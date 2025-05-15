import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Datasets/tip.csv')

x = df['day']
y = df['total_bill']

plt.scatter(x, y)

plt.title('Tips dataset')
plt.xlabel('Days')
plt.ylabel('Total Bill')

plt.show()