import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Datasets/tip.csv')

plt.hist(df['total_bill'])

plt.title('Tips dataset')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')

plt.show()