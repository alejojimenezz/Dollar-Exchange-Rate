import pandas as pd

historic = pd.read_csv("historico.csv")

historic["VALOR"] = (
    historic["VALOR"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

historic["VIGENCIADESDE"] = pd.to_datetime(historic["VIGENCIADESDE"], format="%d/%m/%Y")
historic["VIGENCIAHASTA"] = pd.to_datetime(historic["VIGENCIAHASTA"], format="%d/%m/%Y")

historic["VIGENCIADESDE"] = historic["VIGENCIADESDE"].dt.strftime("%Y-%m-%dT00:00:00.000")
historic["VIGENCIAHASTA"] = historic["VIGENCIAHASTA"].dt.strftime("%Y-%m-%dT00:00:00.000")

historic = historic.rename(
    columns={
        "VALOR": "valor",
        "UNIDAD": "unidad",
        "VIGENCIADESDE": "vigenciadesde",
        "VIGENCIAHASTA": "vigenciahasta"
    }
)

df = pd.read_csv("tasa_cambio.csv")

fullDF = pd.concat([historic, df], ignore_index=True)
fullDF = fullDF.drop_duplicates()

if __name__ == "__main__":
    print(historic)
    print(fullDF)