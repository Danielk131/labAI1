import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/atikagondal/Lab-2023-DAVE3625/main/Lab4/data.csv"

df = pd.read_csv(url, sep=",")
df.head()

corrMatrix = df.corr()
df.plot.scatter(x = 'Var1', y = 'Result')
ax1 = df.plot(kind='scatter', x='Var1', y='Result', color='r')
ax2 = df.plot(kind='scatter', x='Var2', y='Result', color='g', ax=ax1)
ax3 = df.plot(kind='scatter', x='Var3', y='Result', color='b', ax=ax1)

plt.matshow(corrMatrix)
plt.show()

corrMatrix.style.background_gradient(cmap='coolwarm')


