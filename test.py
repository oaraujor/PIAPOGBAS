import modPia
import apicon
import json
import os as term

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
        print("NASQUAD TRADING " + '(' + str(numpag) + '/' + str(tot) + ')' + '\n')
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
        print("'>' para siguiente pagina")
        print("'<' para pagina atras")
        nav = input("\Escriba el simbolo para consultar ").upper()

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

# Example of how to use the modified function:
archivo = 'NASDAQ.txt''NASQAD.txt'
selected_symbol = verOpc(archivo)
if selected_symbol:
    print(f"Símbolo seleccionado: {selected_symbol}")
else:
    print("Ningún símbolo seleccionado.")