números = [[], []]
print('-=' * 30)
for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        números[0].append(n)
        números[0].sort()
    else:
        números[1].append(n)
        números[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {str(números[0]).replace("[", "").replace("]", "")}')
print(f'Os valores ímpares digitados foram:  {str(números[1]).replace("[", "").replace("]", "")}')
