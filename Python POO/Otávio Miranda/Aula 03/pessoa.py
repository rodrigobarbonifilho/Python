from datetime import datetime
from random import randint

class Pessoa:
    ano_atual = datetime.today().year

    def __init__(self, nome: str, idade: int, falando: bool = False, comendo: bool = False) -> None:
        self.nome: str = nome
        self.idade: int = idade
        self.falando: bool = falando
        self.comendo: bool = comendo

    def comer(self, alimento: str):
        if self.falando:
            print(f"{self.nome} não pode comer e falar.")
            return
        if self.comendo:
            print(f"{self.nome} já está comendo.")
            return
        print(f"{self.nome} está comendo {alimento}.")
        self.comendo = True

    def falar(self, assunto: str):
        if self.comendo:
            print(f"{self.nome} não pode falar de boca cheia.")
            return
        if self.falando:
            print(f"{self.nome} já está falando.")
            return
        print(f"{self.nome} está falando sobre {assunto}.")
        self.falando = True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo.")
            return
        self.comendo = False

    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando.")
            return
        self.falando = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        return cls(nome, cls.ano_atual - ano_nascimento)

    @staticmethod
    def gera_id():
        return randint(20000, 29999)
