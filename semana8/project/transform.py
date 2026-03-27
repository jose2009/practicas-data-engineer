from anonymizedf import anonmyze:
import logging

def anonymize_data(df):
    try:
        logging.info("Iniciando anonimimazion de datos..")
        #aplicamos anonimizacion sobre columnas sensibles
        df_anon = anonmyze(
            df,
            {
                "Comisionado": "name",
                "Telefono": "phone_number",
                "Fecha": "date"
            }
        )
        #eliminamos duplicados para evitar posibles correlaciones
        df_anon = df_anon.drop_duplicates()
        logging.info("Anonimizacion completa")
        return df_anon

    except Exception as e:
        logging.error(f"Error en transformacion: {e}")
        raise