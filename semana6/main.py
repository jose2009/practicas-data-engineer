from pytrends.request import TrendReq
import pandas as pd 
import matplotlib.pyplot as plt 

#conectar a google
pytrends = TrendReq(hl = 'es-ES', tz=360)

#terminos
kw_list = ["Fin del mundo", "Calentamiento global", "Terremoto", "Tsunami"]

#ultimos 5 años
pytrends.build_payload(kw_list, timeframe = 'today 5-y')

#obtener datos
data = pytrends.interest_over_time()

#se elimina columna tecnica
if 'isPartial' in data.columns:
    data = data.drop(columns=['isPartial'])

print(data.head())

#grafico
data.plot(figsize = (12,6))
plt.title("Google trends - ultimos 5 años")
plt.xlabel("fecha")
plt.ylabel("popularidad (0-100)")
plt.tight_layout()
plt.show()
plt.savefig("grafico.png")


