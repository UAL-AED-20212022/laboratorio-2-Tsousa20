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

# tem um problema no print, aparece model.nod.nod....
#Comentário Prof.Inês Almeida: Não é um erro, essa string aparece porque eu faço print(n.ref) na Linked List.
#Não se preocupe com esse print(), é para manter
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

# erro: duplica o pais se escolhermos a posição 1
#Não se preocupe com essa questão, é para manter.
def RPII(controlos, lista_paises):
    pais_novo = controlos[1]
    indice = int(controlos[2])
    if controller.inserir_pais_indice(lista_paises, pais_novo, indice):
        lista_paises.traverse_list()


def VNE():
    controller.verificar_numero_elementos(lista_paises)
        # lista_paises.traverse_list() -> isto faz com que apareça a lista


def VP(controlos, lista_paises):
    pais = controlos[1]
    controller.verificar_pais(lista_paises, pais)
        # lista_paises.traverse_list() -> isto faz com que apareça a lista

# tem um problema no print, aparece model.nod.nod....
#Comentário Prof.Inês Almeida: Não é um erro, essa string aparece porque eu faço print(n.ref) na Linked List.
#Não se preocupe com esse print(), é para manter
def EPE(lista_paises):
    elemento_eliminado = controller.eliminar_primeiro_elemento(lista_paises)
    #Comentário Prof.Inês Almeida:Estes prints são aqui e não na LinkedList.
    # As classes que vos dei não são para a alterar.
    print(f"O país {elemento_eliminado} foi elimminado da lista.") 
        # lista_paises.traverse_list() -> isto faz com que apareça a lista

# tem um problema no print, aparece model.nod.nod....
#Comentário Prof.Inês Almeida: Não é um erro, essa string aparece porque eu faço print(n.ref) na Linked List.
#Não se preocupe com esse print(), é para manter
def EUE(lista_paises):
    controller.eliminar_ultimo_elemento(lista_paises)
    #Aqui o que o queremos é retornar é o último elemento da lista.
    #Para isso devem utilizar a função que eu disponibilizo e que retorna o último elemento da lista
    #Esta função deve ser utilizada antes eliminarem o elemento.
    ultimo_elemento = lista_paises.get_last_node()
    print(f"O país {ultimo_elemento} foi eliminado lista.") 
            # lista_paises.traverse_list() -> isto faz com que apareça a lista


# tem um problema no print, se escolhermos o elemento da posiçao 1, nao emite o print formatado
def EP(controlos, lista_paises):
    pais = controlos[1]
    controller.eliminar_determinado_elemento(lista_paises, pais)
        # lista_paises.traverse_list() -> isto faz com que apareça a lista
        
    
