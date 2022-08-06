"""
Getter = Obter Valores
Setter = Setar Valores
"""

from dataclasses import replace


class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome: str = nome
        self.preco: float = preco

    def desconto(self, percentual: float):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    @property
    def nome(self):
        return self._nome

    # Setter
    @preco.setter
    def preco(self, valor: float):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))
        self._preco = valor

    @nome.setter
    def nome(self, valor: str):
        self._nome = valor.title()

if __name__ == "__main__":
    p1 = Produto("Camiseta", 50)
    p1.desconto(10)
    print(p1.nome)

    p2 = Produto("Caneca", "R$15")
    p2.desconto(10)
    print(p2.nome)
        