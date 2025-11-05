import pandas as pd

# Cargar tu archivo dañado
df = pd.read_csv("updateHistory.csv")

# Conservar solo las columnas válidas
df_clean = df[["valor", "unidad", "vigenciadesde", "vigenciahasta"]].copy()

# Convertir las fechas a datetime
df_clean["vigenciadesde"] = pd.to_datetime(df_clean["vigenciadesde"], errors="coerce")
df_clean["vigenciahasta"] = pd.to_datetime(df_clean["vigenciahasta"], errors="coerce")

# Ordenar por fecha de inicio
df_clean = df_clean.sort_values(by="vigenciadesde")

# Eliminar duplicados por valor, unidad y vigenciadesde
df_clean = df_clean.drop_duplicates(subset=["valor", "unidad", "vigenciadesde", "vigenciahasta"])

# Reiniciar índices
df_clean.reset_index(drop=True, inplace=True)

# Guardar el archivo limpio
df_clean.to_csv("updateHistory_clean.csv", index=False)

print("Archivo limpio guardado como updateHistory_clean.csv")
print(df_clean.head(10))