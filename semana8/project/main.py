from extract import extract_data
from transform import anonymize_data
from load import load_to_redshift
import logging

#configuracion basica de logs (sin exponer datos sensibles)
logging.basicConfig(level = logging.INFO)

def main():
    logging.info("iniciando pipeline de datos..")

    #1. extract
    df = extract_data()
    #2. transform (anonimizacion)
    df_anon = anonymize_data(df)
    #3. load (redshift)
    load_to_redshift(df_anon)
    logging.info("pipeline finalizado correctamente")

if __name__ == "__main__":
    main()