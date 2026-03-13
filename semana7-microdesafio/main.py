from modules.utils import get_trends, save_parquet
countries = ["AR","BR","CL","CO","BO"]

def main():
    print("iniciando pipeline de datos..\n")
    for country in countries:
        print(f"Extaryendo datos para{country}")
        #extarcion
        df = get_trends(country)
        #transformacion
        print("Datos obtenidos correctamente")
        #guardar
        save_parquet(df, country)
        #carga
        print(f"Proceso finalizado para {country}\n")
    print("Pipeline completado")

if __name__ == "__main__":
    main()
