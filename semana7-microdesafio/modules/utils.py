#extraemos los datos desde google trends
from pytrends.request import TrendReq
import pandas as pd 

def get_trends(country):
    keywords =["Sea Level", "Weather","Temperatures", "Carbon Dioxide","Global Warming"]
    #conexion a trends
    pytrends = TrendReq()
    pytrends.build_payload(
        kw_list = keywords,
        timeframe = 'today 5-y',
        geo = country
    )
    #extracion
    df = pytrends.interest_over_time()
    #limpieza
    if "IsPartial" in df.columns:
        df = df.drop(columns = ["IsPartial"])
    
    return df

def save_parquet(df, country):
    #guarda el dataframe en formato parquet dentro de data
    path = f"data/data_{country}.parquet"
    df.to_parquet(path)
    print(f"archivo guardado: {path}")