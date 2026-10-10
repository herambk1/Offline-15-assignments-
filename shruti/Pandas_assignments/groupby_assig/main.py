from statistics import median

import pandas as pd

df = pd.read_csv('empsal_part_buck.csv')

salary = df.groupby('dept')["sal"].agg(minsal = "min", maxsal = "max",
                                    meansal = "mean", mediansal = "median",
                                    countsal = "count",sumsal = "sum",)

print(salary)

#Or we can directly pass list of all methods in agg

df1 = df.groupby('dept')['sal'].agg(
    ['min', 'max', 'mean', 'median','count', 'sum']
)
print(df1)