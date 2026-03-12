#conexion a redshift
from sqlalchemy import create_engine
def connect_redshift():
    user = "user"
    password = "password"
    host = "host"
    port = "111"
    database = "fin_del_mundo"

    connection_string = (
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

    )
    engine = create_engine(connection_string)
    return engine

def upload_dataframe(df, table_name):
    engine = connect_redshift()
    df.to_sql(
        table_name,
        engine,
        if_exists = "replace",
        index = true
    )
    print(f"datos cargados en tabla{table_name}")
    