'''
Crie um programa que receba uma lista de números e
 retorne o maior valor dessa lista
'''

numeros = [1, 5, 6, 9, 3, 11, 2]
print(f'Lista: {numeros}')
maior = 0

for numero in numeros:
    if numero > maior:
        print(f'O número {numero} é o maior agora')
        maior = numero

print(f'O maior numero é {maior}')