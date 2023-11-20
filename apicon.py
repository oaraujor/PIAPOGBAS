import requests
import json
from datetime import datetime

# writeFILE(data,archivoNom) #escritura de texto
def writeFILE(texto, tipo, emp):
    '''
    Funcion que escribe los datos proporcionados por la api
    a un archivo .txt

    Param: texto (str)
            type (str) tipo de dato de la api (puede ser
            nombre de empresa, accion etc etc)
    Returns: 0 is existe error al iniciar/escribir un archivo
    '''
    tipo = str(tipo)

    fechaHoy = datetime.now().date()
    fechaHoy = fechaHoy.strftime('%d-%m-%Y')
    archivoNom = 'datosAPI\Data-' + str(fechaHoy) +'-'+ str(tipo) +str(emp)+'.txt'

    try:
        with open(archivoNom, 'w') as file:
            file.write(str(texto))
    except:
        return 0
    

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
        print(data)
        #data_str = str(data)
        #data_str = data_str.replace("'", '"')
        #json_data = json.loads(str(data)) #str(data)
        json_data = json.loads(json.dumps(data))
        return json_data
    
    except requests.RequestException as e:
        print(f"Error making request: {e}")
        return 0

def crearlinkStock(func, symb):
    '''
    funcion que crea el nombre del link, en el cual se pediran los datos
    de la api
    Param:  symb <str> parametro que define la empresa
    Returns: str <link>
             0 <int> as error
    '''
    func = str(func).upper()
    symb = str(symb).upper()
    if func in ['DAILY', 'WEEKLY', 'MONTHLY']:
        link = 'https://www.alphavantage.co/query?function=TIME_SERIES_' + str(func) + '&symbol=' + symb + '&apikey=H59QLA4WONX2VGH4'
        return link
    else:
        return 0


def crearlinkCurr(de, a):
    """
    funcion que crea el nombre del link, en el cual se pediran los datos
    de la api
    Param:  de <str> parametro que define la empresa
            a <str>
    Returns: link (str)
    """
    de = str(de).upper()
    a = str(a).upper()
    link = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+de+'&to_currency='+a+'&apikey=H59QLA4WONX2VGH4'
    return link

def procesarStock(json_data, func):
    if str(func).upper() == "MONTHLY":
        time_series_data = json_data.get("Monthly Time Series")
    elif str(func).upper() == "DAILY":
        time_series_data = json_data.get("Time Series (Daily)")
    elif str(func).upper() == "WEEKLY":
        time_series_data = json_data.get("Weekly Time Series")
    else:
        time_series_data = None

    if time_series_data:
        dates = []
        close_values = []
        for date, values in time_series_data.items():
            dates.append(date)
            close_values.append(float(values.get('4. close', 0)))
    results = [dates,close_values]
    print(len(dates))
    print(len(close_values))
    return results
    

def procesarCurr(jsonDatos):
    try:
        # extraer el valor numerico de '5. Exchange Rate'
        tipoCambio = float(jsonDatos['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        return tipoCambio
    except (KeyError, ValueError):
        # posible error retorna none
        return None

