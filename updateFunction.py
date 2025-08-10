import pandas as pd
from sodapy import Socrata

def updateDB(numLimit, output):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("mcec-87by", limit=numLimit)
    results_df = pd.DataFrame.from_records(results)
    results_df.to_csv(output, index = False)

    return results_df