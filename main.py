import os
import apicon
import modPia

#pendiente
def co_historial(empresa):
    
    print("hola")

def v_graficas(empresa):
    #ver grafica de precio de empresa-divisa x (1 año, 6 meses, 3 meses, ultimo mes)
    while True:
        os.system('cls')
        print("----Precio "+ str(empresa) + "----")
        print("    1. Dia")
        print("    2. Semanal")
        print("    3. Mensual")
        print("    5. Salir")
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
        elif op == '5':
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
        modPia.constGraf(listas)

def c_tipo_cambio():
    while True:
        #consultar tipo de cambio
        archivo = 'curr.txt'
        moneda = modPia.verOpc(archivo)
        link = apicon.crearlinkCurr("MXN", moneda)
        print(link)
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
        print(link)
        data = apicon.makeRequest(link)
        apicon.writeFILE(data,"curr",moneda)
        tipoCambio = apicon.procesarCurr(data)
        os.system('cls')
        mxn = input('Ingrese el monto de MXN a cambiar a ' + str(moneda))
        cambio = mxn * tipoCambio
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

#pendiente
def datestadisticos(empresa):
    print("hola")

def main():
    os.system('cls')
    archivo = "NASDAQ.txt"
    empresa = modPia.verOpc(archivo)
    #empresa es la empresa seleccionada por el usuario
    while True:
        print('------Menu------')
        print("1. Consultar historial de empresa")
        print("2. Ver gráfica de precio de una empresa")
        print("3. Datos estadisticos de una empresa")
        print('Otros:')
        print("4. Consultar un tipo de cambio")
        print("5. Realizar cálculo de cambio de divisa")
        print("6. Salir")
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            co_historial(empresa)
        elif op == 2:
            v_graficas(empresa)
        elif op == 3:
            datestadisticos(empresa)
        elif op == 4:
            c_tipo_cambio()
        elif op == 5:
            cambios_div()
        elif op == 6:
            print("Saliendo del programa. Bye Bye :)")
            break
        else:
            print("Opcion no valida intenta de nuevo")
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
