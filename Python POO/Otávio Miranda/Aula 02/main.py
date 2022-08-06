from pessoa import Pessoa

"""
Métodos de Classe são métodos que a classe usará, geralmente fazendo algum processo e instanciando um objeto após isso.
"""

p1 = Pessoa("Luís", 22)
p2 = Pessoa.por_ano_nascimento("Luís", 2000)

print(p1.idade, p2.idade)
