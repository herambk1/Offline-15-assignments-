import pandas as pd

df = pd.read_excel("employee_dob_practice.xlsx")

df["dob"] = pd.to_datetime(df["dob"])\

todaysdate = pd.Timestamp.today()

df["timedelta"] = todaysdate - df["dob"]

df["age_days"] = df["timedelta"].dt.days

df["age_years"] =  (df['age_days'] / 365)

print(df)

df.to_excel("age_cal.xlsx", index=False)