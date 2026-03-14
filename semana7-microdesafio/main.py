from modules.utils import get_trends, save_parquet
import time
countries = ["AR","BR","CL","CO","BO"]

def main():
    print("iniciando pipeline de datos..\n")
    for country in countries:
        success = False
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:

                print(f"Extaryendo datos para{country}")
                #extarcion
                df = get_trends(country)
                #transformacion
                print("Datos obtenidos correctamente")
                #guardar
                save_parquet(df, country)
                success = True
                break 
            except Exception as e:
                retries += 1
                print("Google bloqueo la request(429). esperando 1 minuto..")
                time.sleep(60)     
        #carga
        print(f"Proceso finalizado para {country}\n")
        time.sleep(15)#espera 15 segundos para evitar el ratelimit
    print("Pipeline completado")

if __name__ == "__main__":
    main()
