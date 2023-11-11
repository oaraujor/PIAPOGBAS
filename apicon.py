import requests
from datetime import datetime

def writeFILE(texto, archivo):
    with open(archivo, 'w') as file:
        file.write(str(texto))

fechaHoy = datetime.now().date()
fechaHoy = fechaHoy.strftime('%d-%m-%Y')
<<<<<<< HEAD
archivoNom = 'datosAPI\Data-' + fechaHoy +'.txt'

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
=======
archivoNom = 'datosAPI\Data-' + fechaHoy +'.

>>>>>>> 1ea79524cfd68e1098a20adb3ce69dab9451c88f
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json()

keys = data.keys()
for i in keys:
    print(str(data[i]))

# writeFILE(data,archivoNom) #escritura de texto
