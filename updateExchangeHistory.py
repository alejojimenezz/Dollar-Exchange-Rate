import pandas as pd

CSVToUpdate = pd.read_csv("updateHistory.csv")

CSVToUpdate["vigenciadesde"] = pd.to_datetime(CSVToUpdate["vigenciadesde"], format="%Y-%m-%d")
CSVToUpdate["vigenciahasta"] = pd.to_datetime(CSVToUpdate["vigenciahasta"], format="%Y-%m-%d")

df = pd.read_csv("DB_fromAPI.csv")

df["vigenciadesde"] = pd.to_datetime(df["vigenciadesde"], format="%Y-%m-%dT00:00:00.000")
df["vigenciahasta"] = pd.to_datetime(df["vigenciahasta"], format="%Y-%m-%dT00:00:00.000")


fullDF = pd.concat([df, CSVToUpdate], ignore_index=True)
fullDF.sort_values(by='vigenciadesde', inplace=True)
fullDF.drop_duplicates(subset=["valor", "unidad", "vigenciadesde", "vigenciahasta"], inplace=True)

fullDF.to_csv("updateHistory.csv", index=False)

if __name__ == "__main__":
    print(CSVToUpdate.head())
    print(type(CSVToUpdate["vigenciadesde"]))
    print(df.head())
    print(type(df["vigenciadesde"]))

    print(fullDF.head())