import psycopg2
import os
import logging

def load_to_redshift(df):
    #carga los datos anonimizados a redshift
    try:
        logging.info("Conectando a Redshift..")

        #uso de variables de entorno 
        conn = psycopg2.connect(
            host = os.getenv("REDSHIFT_HOST"),
            dbname = "BDE_POLITICAS_FIN",
            user = os.getenv("REDSHIFT_USER"),
            password = os.getenv("REDSHIFT_PASSWORD"),
            port = 5439
        )

        cursor = conn.cursor()

        #crear tabla si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS POLITICAS_2050 (
                pais VARCHAR,
                comisionado VARCHAR,
                reduccion_co2 BOOLEAN,
                incremento_p BOOLEAN,
                inversion_arboles BOOLEAN,
                fecha DATE,
                telefono VARCHAR
                );
        """)
        
        #Insertar datos fila por fila
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO POLITICAS_2050 VALUES (%s,%s,%s,%s,%s,%s,%s)
            """, tuple(row))

        conn.commit()
        
        cursor.close()
        conn.close()

        logging.info("Datos caargados en redshift correctamente")

        except Exception as e:
            logging.error(f"error en carga: {e}")
            raise