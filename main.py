import os
import matplotlib.pyplot as plt
import apicon
import modPia

def co_historial(empresa):
    #aqui iria lo de consulta de historial
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
        
        op = int(input("Seleccione una opcion: "))
        if op == 1:
            #grafica de 24 hrs
            link = apicon.crearlinkStock("DAYLY", empresa)
            datos = apicon.makeRequest(link)
            listas = apicon.process_json(datos,'DAYLY')

        elif op == 2:
            #grafica de la semana
            link = apicon.crearlinkStock("WEEKLY", empresa)
            datos = apicon.makeRequest(link)
            listas = apicon.process_json(datos,'DAYLY')
        elif op == 3:
            #grafica del mes
            link = apicon.crearlinkStock("MONTHLY", empresa)
            datos = apicon.makeRequest(link)
            listas = apicon.process_json(datos,'DAYLY')
        elif op == 5:
            #salir
            print("Saliendo...Volviendo al menú")
            return
        else:
            print("Opcion no valida intenta de nuevo. ")
        apicon.writeFILE(listas)
'''
    # Datos de ejemplo
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
    precio = [100, 120, 130, 110, 140, 150]

    # Crear el gráfico de línea
    plt.plot(meses, precio, marker='o', linestyle='-')

    # Agregar etiquetas y título
    plt.xlabel("Meses")
    plt.ylabel("Precio")
    plt.title("Evolución del Precio de la Empresa en los Últimos 6 Meses")

    # Mostrar la gráfica
    plt.grid()  # Agregar una cuadrícula de fondo (opcional)
    plt.show()
'''

def c_tipo_cambio():
    #consultar tipo de cambio
    print("hola")

def cambios_div():
    #realizar calculo la cambio de divisa
    #irian calculos matematicos para el cambio de divisa
    print("hola")

def datestadisticos(empresa):
    print("hola")

def main():
    os.system('cls')
    archivo = "NASDAQ.txt"
    empresa = modPia.verOpc(archivo)
    #empresa es la empresa seleccionada por el usuario

    while True:
        print('------'+str(empresa)+'------')
        print("1. Consultar historial de empresa")
        print("2. Ver gráfica de precio de"+str(empresa))
        print("3. Datos estadisticos de"+ str(empresa))
        print('Otros:')
        print("4. Consultar un tipo de cambio")
        print("5. Realizar cálculo de cambio de divisa")
        print("6. Realizar cálculo de cambio de divisa")
        print("7. Salir")
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
