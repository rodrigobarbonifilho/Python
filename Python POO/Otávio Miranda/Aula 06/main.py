"""
Na programação orientada a objetos clássicas nos temos modificadores de acesso, são eles:
    public, protected e private

    public - Métodos ou Atributos podem ser acessado dentro e fora da classe
    protected - Atributos que só podem ser acessado dentro da classe ou filhas dela
    private - Atributo ou Método só pode ser acessado dentro da classe

No python usamo "_" ou "__" no lugar de private.
Mas o "_" ainda não uma forma muito privda, já o "__" não posiibilita utilizarmos o atributo fora da classe. Então:
_ protected
__ private
"""
import clean_terminal

class BaseDeDados:
    # Método que simula o funcionamento de um método construtor
    def __init__(self):
        self.__dados: dict = {}
    
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id: int, nome: str):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados["clientes"].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados["clientes"][id]

if __name__ == "__main__":
    bd = BaseDeDados()
    bd.inserir_cliente(1, "Otávio")
    bd.inserir_cliente(2, "Miranda")
