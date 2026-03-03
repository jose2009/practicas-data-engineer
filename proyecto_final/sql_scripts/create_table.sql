--creacion de la tabla que almacenará los datos historicos
create table crypto_market_history(
    crypto_name varchar(50),
    date timestamp,     --fecha del dato historico
    price float,
    market_cap float,
    volume float,       --volumen de operaciones
    ingestion_timestamp timestamp   --fecha en que se carga el dato
);