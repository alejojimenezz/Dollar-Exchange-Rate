import pandas as pd

df = pd.read_csv('tasa_cambio.csv')

latestUpdate_pd = df.iloc[0]['vigenciadesde']
latestUpdate_dt = pd.to_datetime(latestUpdate_pd)
latestUpdate = latestUpdate_dt.date()

print(df.iloc[0])
print(latestUpdate)