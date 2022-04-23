import controller
from models.LinkedList import LinkedList

lista_paises = LinkedList()

def main():


    while True:
        controlos = input().split(" ")


        if controlos[0] == "RPI":
            RPI(controlos, lista_paises)

        elif controlos[0] == "RPF":
            RPF(controlos, lista_paises)

        elif controlos[0] == "RPDE":
            RPDE(controlos, lista_paises)

        elif controlos[0] == "RPAE":
            RPAE(controlos, lista_paises)

        elif controlos[0] == "RPII":
            RPII(controlos, lista_paises)

        elif controlos[0] == "VNE":
            VNE()

        elif controlos[0] == "VP":
            VP(controlos, lista_paises)

        elif controlos[0] == "EPE":
            EPE(lista_paises)

        elif controlos[0] == "EUE":
            EUE(lista_paises)

        elif controlos[0] == "EP":
            EP(controlos, lista_paises)


def RPI(controlos, lista_paises):
    pais_novo = controlos[1]
    if controller.inserir_pais_inicio(lista_paises, pais_novo):
        lista_paises.traverse_list()

def RPF(controlos, lista_paises):
    pais_novo = controlos[1]
    if controller.inserir_pais_fim(lista_paises, pais_novo):
        lista_paises.traverse_list()


def RPDE(controlos, lista_paises):
    pais_novo = controlos[1]
    pais_registado = controlos[2]
    if controller.inserir_pais_depois_elemento(lista_paises, pais_novo, pais_registado):
        lista_paises.traverse_list()


def RPAE(controlos, lista_paises):
    pais_novo = controlos[1]
    pais_registado = controlos[2]
    if controller.inserir_pais_antes_elemento(lista_paises, pais_novo, pais_registado):
        lista_paises.traverse_list()


def RPII(controlos, lista_paises):
    pais_novo = controlos[1]
    indice = int(controlos[2])
    if controller.inserir_pais_indice(lista_paises, pais_novo, indice):
        lista_paises.traverse_list()


def VNE():
    count = controller.verificar_numero_elementos(lista_paises)
    print(f"O número de elementos são {count}.")


def VP(controlos, lista_paises):
    pais = controlos[1]
    if controller.verificar_pais(lista_paises, pais) == True:
        print(f"O país {pais} encontra-se na lista.")
    else:
        print(f"O país {pais} não se encontra na lista.")


def EPE(lista_paises):
    elemento_eliminado = controller.eliminar_primeiro_elemento(lista_paises)
    print(f"O país {elemento_eliminado} foi eliminado da lista.")


def EUE(lista_paises):
    ultimo_elemento = controller.eliminar_ultimo_elemento(lista_paises)
    print(f"O país {ultimo_elemento} foi eliminado lista.")
        


def EP(controlos, lista_paises):
    pais = controlos[1]
    if controller.eliminar_determinado_elemento(lista_paises, pais) == True:
        print(f"O país {pais} foi eliminado da lista.")
    else:
        print(f"O país {pais} não se encontra na lista.")
