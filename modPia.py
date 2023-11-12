"""
    Modulo Py donde se enceuntran unicamente las funciones a usar en el main
"""

import os as term
def verArchNasqad():
    """
    funcion que permite visualizar la lista de las empresas NASQAD
    param:  archivo (str) > archivo donde se encuentra la lista nasquad
    return: NONE
    """
    def mostrarListaNasqad(dict, numpag, tot, tamano=5):
        inicio = (numpag - 1) * tamano
        final = inicio + tamano
        term.system('cls')
        print("NASQUAD TRADING "+ '('+str(numpag)+'/'+ str(tot)+')'+'\n')
        print("Simbolo\t\tDescripcion")
        print("------\t\t-----------")

        for abvr, desc in list(dict.items())[inicio:final]:
            print(f"{abvr}\t\t{desc}")

    archivo = 'NASDAQ.txt'
    dict = {}
    with open(archivo, 'r') as file:
        next(file) #saltarse la primera linea del archivo
        for line in file:
            abvr, descrip = line.strip().split('\t')
            dict[abvr] = descrip

    paginasTot = (len(dict) + 4) // 5
    act_pag = 1

    while True:
        mostrarListaNasqad(dict, act_pag, paginasTot)

        nav = input("\nOptions: '>', '<', or 'salir'\n").lower()

        if nav == '>' and act_pag < paginasTot:
            act_pag += 1
        elif nav == '<' and paginasTot > 1:
            act_pag -= 1
        elif nav == 'salir':
            break
        else:
            print("Invalid input. Please enter 'next', 'back', or 'exit'.")