import pandas as pd

CSVToUpdate = pd.read_csv("updateHistory.csv")

df = pd.read_csv("tasa_cambio.csv")

fullDF = pd.concat([df, CSVToUpdate], ignore_index=True)
fullDF = fullDF.drop_duplicates()

fullDF.to_csv("updateHistory.csv")

if __name__ == "__main__":
    print(CSVToUpdate)
    print(df)
    print(fullDF)