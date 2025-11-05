import pandas as pd

CSVToUpdate = pd.read_csv("updateHistory.csv")

# TODO: Update file to format DB_fromAPI to match other csv
df = pd.read_csv("DB_fromAPI.csv")

fullDF = pd.concat([df, CSVToUpdate], ignore_index=True)
fullDF["vigenciadesde"] = pd.to_datetime(fullDF["vigenciadesde"], errors="coerce")
fullDF["vigenciahasta"] = pd.to_datetime(fullDF["vigenciahasta"], errors="coerce")
fullDF.sort_values(by='vigenciadesde', inplace=True)
# fullDF = pd.read_csv("updateHistory.csv") ##
fullDF.drop_duplicates(subset=["valor", "unidad", "vigenciadesde", "vigenciahasta"], inplace=True)

fullDF.to_csv("updateHistory.csv", index=False)

if __name__ == "__main__":
    print(CSVToUpdate.head())
    print(df.head())
    print(fullDF.head())