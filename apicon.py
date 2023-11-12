import requests
import json
from datetime import datetime

# writeFILE(data,archivoNom) #escritura de texto
def writeFILE(texto):
    '''
    Funcion que escribe los datos proporcionados por la api
    a un archivo .txt

    Param: texto (str)
    Returns: 0 is existe error al iniciar/escribir un archivo
    '''
    fechaHoy = datetime.now().date()
    fechaHoy = fechaHoy.strftime('%d-%m-%Y')
    archivoNom = 'datosAPI\Data-' + fechaHoy +'.txt'

    try:
        with open(archivoNom, 'w') as file:
            file.write(str(texto))
    except:
        return 0
    
    chages 

def makeRequest(url):
    '''
    Funcion encargada de realizar los API calls
    Param: url (txt)
            Ej:'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
    Returns: 0 si error alguno (200)
             data (formato json)
    '''
    try:
        r = requests.get(url)
        r.raise_for_status()  # Bandera de HTTPError para errores potenciales
        data = r.json()
        return data
    
    except requests.RequestException as e:
        print(f"Error making request: {e}")
        return 0

def crearlink(symb, int):
    return 0

#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
#datos = makeRequest(url)
#writeFILE(str(datos))


