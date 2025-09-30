import pandas as pd

# CSVToUpdate = pd.read_csv("updateHistory.csv")

# df = pd.read_csv("DB_fromAPI.csv")

# fullDF = pd.concat([df, CSVToUpdate], ignore_index=True)
# fullDF.sort_values(by='vigenciadesde', inplace=True)
fullDF = pd.read_csv("updateHistory.csv") ##
fullDF.drop_duplicates(inplace=True)

fullDF.to_csv("updateHistory.csv")

if __name__ == "__main__":
    # print(CSVToUpdate)
    # print(df)
    print(fullDF)