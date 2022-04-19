import controller
from models import LinkedList

lista_paises = LinkedList()

def main():
    

    while True:
        controlos = input().split(" ")


        if controlos[0] == "RPI":
            RPI(controlos)
            
        elif controlos[0] == "RPF":
            RPF(controlos)
            
        elif controlos[0] == "RPDE":
            RPDE(controlos)
            
        elif controlos[0] == "RPAE":
            RPAE(controlos)
            
        elif controlos[0] == "RPII":
            RPII(controlos)

        elif controlos[0] == "VNE":
            VNE(controlos)

        elif controlos[0] == "VP":
            VP(controlos)

        elif controlos[0] == "EPE":
            EPE(controlos)

        elif controlos[0] == "EUE":
            EUE(controlos)

        elif controlos[0] == "EP":
            EP(controlos)

    
def RPI(controlos, lista_paises):
    pais_novo = controlos[1]
    lista_paises.insert_at_start(pais_novo)
            