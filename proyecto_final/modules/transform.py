#importacion datetime para trabajar con fechas
from datetime import datetime

def transform_data(data, crypto_name):
    #extraemos los arrays del json
    prices = data["prices"]
    market_caps = data["market_caps"]
    volumes = data["total_volumes"]

    records = [] #lista donde se guarde los registros finales

    #se recorre todos los dias
    for i in range(len(prices)):
        #se convierte el timestamp de milisengundo a segundos
        timestamp = prices[i][0]/1000
        #se convierte el timestamp en fecha
        date = datetime.fromtimestamp (timestamp)
        #registro
        record ={
            "crypto_name": crypto_name,
            "date": date,
            "price": prices[i][1],
            "market_cap": market_caps [i][1],
            "volume": volumes [i][1],
            #fecha en que se ejecuta el pipeline
            "ingestion_timestamp": datetime.now()
        }
        #se agrega el registro a la lista
        records.append(record)

    return records