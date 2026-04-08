#libreria para conexion a bases postgresql/redshift
import psycpog2

def load_to_redshift(df):
    try:
        conn = psycpog2.connect(
            host = "host",
            dbname = "db",
            user = "user",
            password = "password",
            port = 5439
        )
        cursor = conn.cursor()

        #insertar datos fila por fila
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO crypto_market_history (
                    crypto_name, date, price, market_cap, volume, ingestion_timestamp
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (crypto_name, date) DO UPDATE SET
                    price = EXCLUDED.price,
                    market_cap = EXCLUDED.market_cap,
                    volume = EXCLUDED.volume,
                    ingestion_timestamp = EXCLUDED.ingestion_timestamp;
            """, (
                row["crypto_name"],
                row["date"],
                row["price"],
                row["market_cap"],
                row["volume"],
                row["ingestion_timestamp"]
            ))
        conn.commit()
        cursor.close()
        conn.close()

        print("Datos cargados en Redshift correctamente.")

    except Exception as e:
        print("Simulacion de carga a Redshift (sin credenciales).")
        print(f"Detalle: {e}")