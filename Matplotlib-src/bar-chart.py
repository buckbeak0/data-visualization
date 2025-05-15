import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Datasets/tip.csv')

plt.bar(df['day'], df['total_bill'])

plt.title('Tis dataset')
plt.xlabel('Days')
plt.ylabel('Bill')

plt.show()