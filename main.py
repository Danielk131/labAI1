import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/umaimehm/Intro_to_AI_2021/main/Lab1/stud.csv'
df = pd.read_csv(url, sep=",")
df.head()
#print(df)
#print(df.describe())
df = df.replace(r'^\s*$', np.nan, regex=True)
df["Age"].replace(np.nan, 0, inplace=True)
df.dropna(inplace=True)
df['Age'] = df['Age'].astype(str).astype(int)
df['hrsStudy'] = df['hrsStudy'].astype(str).astype(int)
z_scores = stats.zscore(df["FinalGrade"])
abs_z_scores = np.abs(z_scores)
df.drop(df[abs_z_scores > 3].index, inplace=True)
tabell = df.info()
df = df.reset_index(drop=True)

conditions = [
    (df["FinalGrade"] <= 50),
    (df["FinalGrade"] >50) & (df["FinalGrade"] <= 60),
    (df["FinalGrade"] >60) & (df["FinalGrade"] <= 70),
    (df["FinalGrade"] >70) & (df["FinalGrade"] <= 80),
    (df["FinalGrade"] >80) & (df["FinalGrade"] <= 90),
    (df["FinalGrade"] >90)]

values = ["F", "E", "D", "C", "B", "A"]

df["Grade"] = np.select(conditions, values)
df.head(5)

df_gradeCount = df.groupby("Grade").count()

df_gradeCount["FinalGrade"].plot.bar()

df["FinalGrade"].plot()
plt.show()
#print(df)
