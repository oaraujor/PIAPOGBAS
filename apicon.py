import requests
from datetime import datetime

fechaHoy = datetime.now().date()
fechaHoy = fechaHoy.strftime('%d-%m-%Y')
archivoNom = 'datosAPI\Data-' + fechaHoy +'.txt'

def writeFILE(texto, archivo):
    with open(archivo, 'w') as file:
        file.write(str(texto))

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json()
writeFILE(data,archivoNom)
