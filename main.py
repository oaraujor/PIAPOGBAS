import os
import apicon
import modPia
import pandas as pd
from openpyxl import Workbook
from datetime import datetime

def v_graficas(empresa):
    #ver grafica de precio de empresa-divisa x (1 año, 6 meses, 3 meses, ultimo mes)
    while True:
        os.system('cls')
        print("----Precio "+ str(empresa) + "----")
        print("    1. Dia")
        print("    2. Semanal")
        print("    3. Mensual")
        print("    4. Salir")
        op = input("Seleccione una opcion: ")
        if op == '1':
            #grafica de 24 hrs
            tipo = "DAILY"
        elif op == '2':
            #grafica de la semana
            tipo = "WEEKLY"
        elif op == '3':
            #grafica del mes
            tipo = "MONTHLY"
        elif op == '4':
            #salir
            os.system('cls')
            return
        else:
            print("Opcion no valida intenta de nuevo. ")
            continue

        link = apicon.crearlinkStock(tipo, empresa)
        datos = apicon.makeRequest(link)
        listas = apicon.procesarStock(datos,tipo)
        apicon.writeFILE(listas, tipo, empresa)
        modPia.constGraf(listas, empresa)

def c_tipo_cambio():
    while True:
        #consultar tipo de cambio
        archivo = 'curr.txt'
        moneda = modPia.verOpc(archivo)
        link = apicon.crearlinkCurr("MXN", moneda)
        #print(link)
        data = apicon.makeRequest(link)
        apicon.writeFILE(data,"curr",moneda)
        tipoCambio = apicon.procesarCurr(data)
        os.system('cls')
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

def cambios_div():
    while True:
        #hacer un tipo de cambio de divisa tipo de cambio
        archivo = 'curr.txt'
        moneda = modPia.verOpc(archivo)
        link = apicon.crearlinkCurr("MXN", moneda)
        data = apicon.makeRequest(link)
        apicon.writeFILE(data,"curr",moneda)
        tipoCambio = apicon.procesarCurr(data)
        os.system('cls')
        mxn = input('Ingrese el monto de MXN a cambiar a ' + str(moneda)+" ")
        cambio = int(mxn) * tipoCambio
        print(str(mxn) + " Pesos Mexicanos equivalen a: "+ str(cambio) +str(moneda) )
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

def datestadisticos(empresa):
    os.system('cls')
    while True:
        print("------Datos Estadisticos------")
        print("    1. Estadísticas Diarias")
        print("    2. Estadísticas Semanales")
        print("    3. Estadísticas Mensuales")
        print("    4. Salir")
        op = input("Seleccione una opción: ")

        if op == '1':
            tipo_periodo = "DAILY"
        elif op == '2':
            tipo_periodo = "WEEKLY"
        elif op == '3':
            tipo_periodo = "MONTHLY"
        elif op == '4':
            os.system('cls')
            return
        else:
            print("Opción no válida. Intenta de nuevo.")
            continue

        link = apicon.crearlinkStock(tipo_periodo, empresa)
        datos = apicon.makeRequest(link)
        listas = apicon.procesarStock(datos, tipo_periodo)

        # Crear archivo de Excel
        datos = listas[1]
        promedio, dvs, volatilidad = modPia.datosEst(datos, op)
        os.system('cls')
        print(f"El precio promedio de {empresa} es:  {promedio}")
        print(f"La desviacion estandar de {empresa} es:  {dvs}")
        print(f"La volatilidad de la empresa: {empresa} es:  {volatilidad}")
        crear_excel(listas, tipo_periodo, empresa)

        put = input("Desea hacer otra consulta? SI/NO").upper()
        if put == 'NO':
            break
        elif put == 'SI':
            continue
    return 


def crear_excel(datos, tipo_periodo, empresa):
    # Crear un frame con los datos
    df = pd.DataFrame(datos)

    # Obtener la fecha actual para incluirla en el nombre del archivo
    fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Crear un libro de trabajo de Excel
    wb = Workbook()

    # Añadir los datos al libro de trabajo
    ws = wb.active
    # usar la columna de nombres de dataframe
    ws.append(df.columns.tolist())
    for row in df.itertuples(index=False):
        ws.append(list(row))
    # Guardar el libro de trabajo como un archivo Excel
    nombre_archivo = f"{empresa}_{tipo_periodo}_{fecha_actual}.xlsx"
    wb.save(nombre_archivo)

    print(f"Archivo de Excel '{nombre_archivo}' creado con éxito.")
    

def main():
    os.system('cls')
    archivo = "NASDAQ.txt"
    empresa = modPia.verOpc(archivo)
    #empresa es la empresa seleccionada por el usuario
    while True:
        os.system('cls')
        print('------'+ str(empresa) +'------')
        print("1. Ver gráfica de precio de " + str(empresa))
        print("2. Datos estadisticos de "+ str(empresa))
        print('Otros:')
        print("3. Consultar un tipo de cambio")
        print("4. Realizar cálculo de cambio de divisa")
        print("5. Salir")
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            v_graficas(empresa)
        elif op == 2:
            datestadisticos(empresa)
        elif op == 3:
            c_tipo_cambio()
        elif op == 4:
            cambios_div()
        elif op == 5:
            print("Saliendo del programa. Bye Bye :)")
            break
        else:
            print("Opcion no valida intenta de nuevo")
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
