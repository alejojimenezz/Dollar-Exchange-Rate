import pandas as pd

df = pd.read_csv('tasa_cambio.csv')

latestValue = df.iloc[0]['valor']

print(latestValue)
print(type(latestValue))