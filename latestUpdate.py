import pandas as pd
import datetime

def latestUpdate(df):
    date_pd = df.iloc[0]['vigenciadesde']
    date_dt = pd.to_datetime(date_pd)
    date = date_dt.date()
    return date # , value


df = pd.read_csv('tasa_cambio.csv')

latestUpdate_pd = df.iloc[0]['vigenciadesde']
latestUpdate_dt = pd.to_datetime(latestUpdate_pd)
latestUpdate = latestUpdate_dt.date()

print(df.iloc[0])
print(latestUpdate)

today = datetime.date.today()

if(latestUpdate != today):
    print("Database is up to date.")
else:
    print("Database is NOT up to date.")