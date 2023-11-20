import modPia
import apicon
import json
import os as term
"""
while True:
        #consultar tipo de cambio
        archivo = 'curr.txt'
        moneda = modPia.verOpc(archivo)
        link = apicon.crearlinkCurr("MXN", moneda)
        print(link)
        data = apicon.makeRequest(link)
        apicon.writeFILE(data,"curr",moneda)
        tipoCambio = apicon.procesarCurr(data)
        term.system('cls')
        print("1 Peso Mexicano(MXN) equivale a: "+ str(tipoCambio) +str(moneda) )

        imp = input('Desea consultar otro tipo de cambio? ("SI", NO")')
        imp = imp.upper()
        if imp == 'NO':
            break
        elif imp == 'SI':
            continue
        else:
            valid = False
            while not valid:
                a = input('Entrada no valida - Selecione "SI" o "NO"')
                if a in ["SI","NO"]:
                    valid = True
                else:
                    valid = False
"""

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

    #result = json.dumps([dates, close_values])
    results = [dates,close_values]
    print(len(dates))
    print(len(close_values))
    return results

