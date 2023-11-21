import os as term
import statistics
import matplotlib.pyplot as plt


def verOpc(archivo):
    """
    Función que permite visualizar la lista de las empresas NASQAD y seleccionar un símbolo.
    :param archivo: (str) Archivo donde se encuentra la lista NASQAD.
    :return: (str) Símbolo seleccionado por el usuario.
    """
    def mostrarListaNasqad(dict, numpag, tot, tamano=5):
        inicio = (numpag - 1) * tamano
        final = inicio + tamano
        term.system('cls')
        print("NASQUAD - Tipo de Cambio " + '(' + str(numpag) + '/' + str(tot) + ')' + '\n')
        print("Simbolo\t\tDescripcion")
        print("------\t\t-----------")

        for abvr, desc in list(dict.items())[inicio:final]:
            print(f"{abvr}\t\t{desc}")

    symbols = {}
    archivo = str(archivo)
    with open(archivo, 'r') as file:
        next(file)  # Saltarse la primera línea del archivo
        for line in file:
            abvr, descrip = line.strip().split('\t')
            symbols[abvr] = descrip
    paginasTot = (len(symbols) + 4) // 5
    act_pag = 1
    while True:
        mostrarListaNasqad(symbols, act_pag, paginasTot)
        print("Opciones: 'salir' para salir")
        print("           '>' para siguiente pagina")
        print("           '<' para pagina atras")
        nav = input("Escriba el simbolo de una empresa para consultar ").upper()
        if nav == 'SALIR':
            break
        elif nav in symbols:
            return nav
        elif nav == '>' and act_pag < paginasTot:
            act_pag += 1
        elif nav == '<' and paginasTot > 1:
            act_pag -= 1
        elif nav == 'salir':
            break
        else:
            print("Simbolo no valido. Por favor, ingrese '>', '<','salir' o escoja in simbolo de la lista")

def validacion_Emp(emp, archivo='NASQAD.txt'):
    try:
        with open(archivo, 'r') as file:
            lines = file.readlines()[1:]  # saltarse el titulo
            symbols = [line.split('\t')[0] for line in lines]

            if emp in symbols:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"Error: Archivo '{archivo}' no encontrado")
        return False
    
def constGraf(lista, empresa):
        intervalos = lista[0]
        precio = lista[1]

        # Crear el gráfico de línea
        plt.plot(intervalos, precio, marker='o', linestyle='-')

        # Agregar etiquetas y título
        plt.xlabel("Fecha")
        plt.ylabel("Precio")
        plt.title("Evolución del Precio de la Empresa " + str(empresa))

        # Mostrar la gráfica
        plt.grid()  # Agregar una cuadrícula de fondo (opcional)
        plt.show()

def datosEst(listaDeDatos, tipo):
    # Calcular prom 
    mean_price = statistics.mean(listaDeDatos)

    # Calcular std 
    std_deviation = statistics.stdev(listaDeDatos)

    if tipo == 'DAILY':
        volatility = std_deviation * (252**0.5)
    elif tipo == 'WEEKLY':
        volatility = std_deviation * (52**0.5)
    elif tipo == 'MONTHLY':
        volatility = std_deviation * (12**0.5)
    else:
        volatility = 0
    return mean_price, std_deviation, volatility