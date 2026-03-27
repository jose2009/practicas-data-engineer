from anonymizedf.anonymizedf import anonymize
import logging

def anonymize_data(df):
    """
    Aplica anonimización sobre datos sensibles (PII)
    """

    try:
        logging.info("🔐 Iniciando anonimización de datos...")

        # Crear instancia del anonimizador
        anon = anonymize(df)

        # Aplicar métodos específicos por columna
        anon.fake_names("Comisionado")
        anon.fake_phone_numbers("Telefono")
        anon.fake_dates("Fecha")

        # Obtener dataframe anonimizado
        df_anon = anon.df

        # Eliminamos duplicados
        df_anon = df_anon.drop_duplicates()

        logging.info("✅ Anonimización completada")

        return df_anon

    except Exception as e:
        logging.error(f"❌ Error en transformación: {e}")
        raise