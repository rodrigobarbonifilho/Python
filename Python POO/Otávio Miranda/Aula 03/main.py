from pessoa import Pessoa

"""
Métodos Estáticos são métodos que a classe e o objeto podem usar, são métodos que funcionam como funções normais mas que por motivos de lógica e organização do código seria bom usá-lo dentro da classe.
"""

p1 = Pessoa("Luís", 22)
p2 = Pessoa.por_ano_nascimento("Luís", 2000)

print(p1.idade, p2.idade)
