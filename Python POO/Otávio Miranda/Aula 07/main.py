from os import system
from time import sleep
from classes import *

"""
Associação: Fazer classes conversar com outras
"""

if __name__ == "__main__":
    system("cls")

    def linha():
        print("-=" * 20)

    linha()
    print("Associação".center(40))
    linha()

    escritor = Escritor("Rodrigo")
    caneta = Caneta("BIC")
    maquina = MaquinaDeEscrever()

    escritor.ferramenta = caneta
    escritor.ferramenta.escrever()

    # opcoes = ["Caneta", "Máquina de Escrever"]
    # while True:
    #     system("cls")
    #     linha()
    #     for index, opcao in enumerate(opcoes):
    #         print(index+1, opcao)
    #     linha()
        
    #     ferramenta_a_ser_usada = int(input("Qual ferramenta você deseja usar? "))-1

    #     escritor.ferramenta = caneta if ferramenta_a_ser_usada == 0 else maquina
    #     escritor.usar_ferramenta()
    #     sleep(1)
