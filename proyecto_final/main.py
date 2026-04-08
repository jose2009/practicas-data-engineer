import pandas as pd 
#se importa la funciones
from modules.extract import extract_data
from modules.transform import transform_data
from modules.load import load_to_redshift
#criptos que vamos a usar
CRYPTOS = ["bitcoin", "ethereum", "solana"]

def main():
    all_data = [] #se acumulan los registros

    #se recorren todas las criptos
    for crypto in CRYPTOS:
        print(f"Extrayendo datos de {crypto}..")
        #extrae datos
        raw_data = extract_data(crypto)
        #si la API respondio correctamente
        if raw_data:
            #transformo datos
            transformed = transform_data(raw_data, crypto)
            #se agrega al cojunto general
            all_data.extend(transformed)
    #se convierte la lista final en dataframe
    df = pd.DataFrame(all_data)
    #se guarda en csv
    df.to_csv("crypto_market_history.csv", index=False)

    #eliminar duplicados
    df = df.drop_duplicates(subset=[¨"crypto_name","date"])

    #eliminar nulos
    df = df.dropna()

    
    print("Proceso finalizado corectamente.")

if __name__ == "__main__":
    main()
    load_to_redshift(df)