import pandas as pd
from sodapy import Socrata

limit = 2000
output = "tasa_cambio.csv"

def updateDB(limit, output):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("mcec-87by", limit=limit)
    results_df = pd.DataFrame.from_records(results)
    results_df.to_csv(output, index = False)

    return results_df