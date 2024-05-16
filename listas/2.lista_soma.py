'''
Crie um programa que receba uma lista de números e
 retorne a soma de todos os valores.
'''

numeros = [1, 5, 3, 9]
print(f'Lista: {numeros}')
soma = 0

for numero in numeros:
    soma += numero

print(f' somados dá {soma}')