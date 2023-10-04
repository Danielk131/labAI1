import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from pandas.api.types import is_numeric_dtype

url = "https://raw.githubusercontent.com/atikagondal/Lab-2023-DAVE3625/main/Lab3/data/flight.csv"

df = pd.read_csv(url)

df['datetime_val'] = pd.to_datetime(df['datetime_val'], errors='coerce')
df['dep_time'] = pd.to_datetime(df['dep_time'], errors='coerce')
df['arr_time'] = pd.to_datetime(df['arr_time'], errors='coerce')
df['sched_arr_time'] = pd.to_datetime(df['sched_arr_time'], errors='coerce')
df["air_time"] = df["arr_time"]-df["dep_time"]

for index, row in df.iterrows():
    #if arr_time is less then dep_time
    if (row['arr_time']<row['dep_time']):
        #add one day to arr_time
        df.loc[index, 'arr_time'] = (row['arr_time'])+ datetime.timedelta(days=1)
    if (row['sched_arr_time']<row['dep_time']):
        df.loc[index, 'sched_arr_time'] = (row['sched_arr_time'])+ datetime.timedelta(days=1)

df["air_time"] = df["dep_time"]-df["arr_time"]
df["Delay"] = df["arr_time"]-df["sched_arr_time"]


for index, row in df.iterrows():
    if (row["air_time"].days<0):
        df.loc[index, "air_time"] = datetime.timedelta(days=1) - row["air_time"] - datetime.timedelta(abs(row['air_time'].days))

for index, row in df.iterrows():
    if (row["Delay"].days>=0):
        df.loc[index, "percent_delay"] = (100 * row["Delay"])/row["air_time"]

def remove_outlier(df):
    low = .05
    high = .95
    quant_df = df.quantile([low, high])
    if is_numeric_dtype(df):
        df = df[(df > quant_df.loc[low]) & (df < quant_df.loc[high])]
    return df

df["percent_delay"] = remove_outlier(df["percent_delay"])
print(df["percent_delay"])





print(df["dep_time"].head())
print(df["arr_time"].head())
print(df["air_time"].head())
print(df["Delay"].head())




