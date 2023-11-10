import requests
from datetime import datetime

def writeFILE(texto, archivo):
    with open(archivo, 'w') as file:
        file.write(str(texto))

fechaHoy = datetime.now().date()
fechaHoy = fechaHoy.strftime('%d-%m-%Y')
archivoNom = 'datosAPI\Data-' + fechaHoy +'.

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json()
writeFILE(data,archivoNom)
