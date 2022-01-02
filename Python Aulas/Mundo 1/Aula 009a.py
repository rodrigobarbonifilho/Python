frase = 'Curso em Video Python'

#Fatiamento

print(frase[:5])

print(frase[15:])

print(frase[9::3])

print()

#Analise

print(len(frase))

print(frase.count('o',0,13))

print(frase.find('deo'))

print(frase.find('Cur'))

print(frase.find('Android'))

print('Curso' in frase)

print()

#Transformaçoes

print(frase.replace('Python','Android'))

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

print(frase.strip())

#Divisao

print(frase.split())

#Junção

print('-'.join(frase))
