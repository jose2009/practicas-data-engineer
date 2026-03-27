import pandas as pd 
import logging

def extract_data():
    url = "https://raw.githubusercontent.com/CoderContenidos/Data.Engineering/main/Semana%208/Datos_Microdesafio_Semana8_DE.csv"

    try:
        logging.info("extrayendo datos desde fuente externa..")
        df = pd.read_csv(url)
        #validacion basica de esquema
        expected_columns = [
            'Pais', 'Comisionado', 'Reduccion_CO2',
            'Incremento_P', 'Inversion_arboles','Fecha', 'Telefono'
        ]
        if not all(col in df.columns for col in expected_columns):
            raise ValueError ("El schema no coincide con lo esperado")
        
        logging.info("Datos extraidos correctamente")

        return df 
    except Exception as e:
        logging.error(f"Error en extraccion: {e}")
        raise
