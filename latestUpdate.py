import pandas as pd
import datetime

def latestUpdate(df):

    date_pd = df.iloc[0]['vigenciadesde']
    date_dt = pd.to_datetime(date_pd)
    date = date_dt.date()

    value = df.iloc[0]['valor']

    today = datetime.date.today()

    if(latestUpdate != today):
        upToDate = "Database is NOT up to date."
    else:
        upToDate = "Database is up to date."

    return date, value, upToDate


# df = pd.read_csv('tasa_cambio.csv')

# date, value, upToDate = latestUpdate(df)

# print(date)
# print(value)
# print(upToDate)