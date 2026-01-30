import pandas as pd
import datetime

def latestUpdate(df):

    date_pd = df.iloc[0]['vigenciadesde']
    date_dt = pd.to_datetime(date_pd)
    date = date_dt.date()

    value = df.iloc[0]['valor']

    today = datetime.date.today()

    if(date != today):
        upToDate = "Database is NOT up to date."
    else:
        upToDate = "Database is up to date."

    return date, value, upToDate

if __name__ == "__main__":
    
    df = pd.read_csv('DB_fromAPI.csv')

    date, value, upToDate = latestUpdate(df)

    print(date)
    print(value)
    print(upToDate)