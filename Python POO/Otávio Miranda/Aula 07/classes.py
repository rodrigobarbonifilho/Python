class Caneta:
    def __init__(self, marca: str):
        self.__marca: str = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print("Caneta está escrevendo...")

class MaquinaDeEscrever:
    def __init__(self):
        pass

    def escrever(self):
        print("Máquina de Escrever está escrevendo...")

class Escritor:
    def __init__(self, nome: str):
        self.__nome: str = nome
        self.__ferramenta: Caneta | MaquinaDeEscrever | None = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta: Caneta | MaquinaDeEscrever):
        self.__ferramenta = ferramenta
