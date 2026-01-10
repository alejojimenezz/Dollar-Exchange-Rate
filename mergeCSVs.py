import pandas as pd
from datetime import datetime

def limpiar_valor(valor):
    if isinstance(valor, str):
        return valor.replace('$', '').replace(',', '').strip()
    return str(valor)

def convertir_fecha(fecha_str):
    if isinstance(fecha_str, str):
        if 'T' in fecha_str:
            return fecha_str.split('T')[0]
        
        try:
            fecha_obj = datetime.strptime(fecha_str, '%d/%m/%Y')
            return fecha_obj.strftime('%Y-%m-%d')
        except:
            pass
    
    return fecha_str

df_historico = pd.read_csv('historico.csv')
df_historico['valor'] = df_historico['VALOR'].apply(limpiar_valor)
df_historico['unidad'] = df_historico['UNIDAD']
df_historico['vigenciadesde'] = df_historico['VIGENCIADESDE'].apply(convertir_fecha)
df_historico['vigenciahasta'] = df_historico['VIGENCIAHASTA'].apply(convertir_fecha)

df_historico = df_historico[['valor', 'unidad', 'vigenciadesde', 'vigenciahasta']]

df_api = pd.read_csv('DB_fromAPI.csv')
df_api['vigenciadesde'] = df_api['vigenciadesde'].apply(convertir_fecha)
df_api['vigenciahasta'] = df_api['vigenciahasta'].apply(convertir_fecha)
df_api['valor'] = df_api['valor'].astype(str)

df_combinado = pd.concat([df_historico, df_api], ignore_index=True)
df_combinado['valor'] = df_combinado['valor'].astype(float)
df_combinado = df_combinado.drop_duplicates(subset=['vigenciadesde'], keep='first')

df_combinado['vigenciadesde_dt'] = pd.to_datetime(df_combinado['vigenciadesde'])
df_combinado = df_combinado.sort_values('vigenciadesde_dt', ascending=False)

df_combinado = df_combinado.drop('vigenciadesde_dt', axis=1)

df_combinado['vigenciahasta'] = pd.to_datetime(df_combinado['vigenciahasta']).dt.strftime('%Y-%m-%d')
df_combinado['vigenciadesde'] = pd.to_datetime(df_combinado['vigenciadesde']).dt.strftime('%Y-%m-%d')

df_combinado['vigenciadesde'] = df_combinado['vigenciadesde'] + 'T00:00:00.000'
df_combinado['vigenciahasta'] = df_combinado['vigenciahasta'] + 'T00:00:00.000'

df_combinado.to_csv('FullExchangeRate.csv', index=False)

print(f"Total de registros: {len(df_combinado)}")
print(f"Fecha más reciente: {df_combinado.iloc[0]['vigenciadesde'][:10]}")
print(f"Fecha más antigua: {df_combinado.iloc[-1]['vigenciadesde'][:10]}")

print(df_combinado.head())