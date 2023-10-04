import re

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/atikagondal/Lab-2023-DAVE3625/main/Lab%202/data/Titanic.csv"

df = pd.read_csv(url, sep=",")

#Fyll opp alle tomme aldre/Fare med median nummer
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())
#Bytte NaN med S
df["Embarked"].replace(np.nan, "S", inplace=True)
#Legg til en ny attributt har kabin
df["HasCabin"] = df.Cabin.isnull()
#Siden vi får omvendt verdier må vi invertere tabellen for å få riktige verdier
a_series = pd.Series(df["HasCabin"])
inv = ~a_series
df["HasCabin"] = inv

#Lag en ny rad med tittel (mr / mrs), leter etter første mellomrom i navn
df["Title"] = df.Name.apply(lambda x: re.search(' ([A-Z][a-z]+)\.', x).group(1))
#Erstatt Mlle med ms og Mme med Mr
df["Title"] = df["Title"].replace({"Mlle": "Ms", "Mme": "Mr"})
#Erstatt alle de under med Unique
df["Title"] = df["Title"].replace({"Capt", "Sir", "Lady", "Don", "Major", "Col", "Ms", "Dr", "Rev", "Countess", "Jonkheer", "Dona"}, "Unique")
print(df["Title"].value_counts())

sns.countplot(x="Title", data=df)
plt.xticks(rotation=45)

df["CatAge"] = pd.qcut(df["Age"], q = 4, labels=False)
df["CatFare"] = pd.qcut(df["Fare"], q = 4, labels=False)

df = df.drop(["Name", "Fare", "Cabin", "Ticket"], axis=1)
#Gjør om til numeriske verdier
df_dum = pd.get_dummies(df, drop_first=True)
print(df_dum.head())
plt.show()
print(df.head)
#print(df.isna().sum())