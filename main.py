import os
import matplotlib.pyplot as plt


def co_accion():
    #aqui iria lo de consulta de accion
    print("hola")

def co_empresa():
    #aqui iria lo de consulta de empresa
    print("hola")

def co_historial():
    #aqui iria lo de consulta de historial
    print("hola")

def v_graficas():
    #ver grafica de precio de empresa-divisa x (1 año, 6 meses, 3 meses, ultimo mes)
    print("hola")
    while True:
        print("----Precio Empresa-Divisa----")
        print("    1. Un Año ")
        print("    2. 6 Meses ")
        print("    3. 3 Meses ")
        print("    4. Ultimo mes ")
        print("    5. Salir")
        
        op = int(input("Seleccione una opcion: "))
        if op == 1:
            #grafica de un año
            print("hola")
        elif op == 2:
            #grafica de 6 meses
            print("hola")
        elif op == 3:
            #grafica de 3 meses
            print("hola")
        elif op == 4:
            #grafica del ultimo mes
            print("hola")
        elif op == 5:
            #salir
            print("Saliendo...Volviendo al menú")
            return
        else:
            print("Opcion no valida intenta de nuevo. ")

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


def main():

    while True:
        print("------Menu------")
        print("1. Consultar acción de 'empresa' ahorita")
        print("2. Consultar empresa")
        print("3. Consultar historial")
        print("4. Ver gráfica de precio de empresa-divisa")
        print("5. Consultar tipo de cambio")
        print("6. Realizar cálculo de cambio de divisa")
        print("7. Salir")
        op = int(input("Ingrese una opcion: "))

        if op == 1:
            co_accion()
        elif op == 2:
            co_empresa()
        elif op == 3:
            co_historial()
        elif op == 4:
            v_graficas()
        elif op == 5:
            c_tipo_cambio()
        elif op == 6:
            cambios_div()
        elif op == 7:
            print("Saliendo del programa. Bye Bye :)")
            break
        else:
            print("Opcion no valida intenta de nuevo")
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
