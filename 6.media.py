'''
Escreva um programa que calcule a média aritmética
 de uma lista de números.
'''

numeros = int(input("Informe a lista de numeros separados por vírgula: "))
soma = 0.0
for numero in numeros:
    soma += numero
print(f"A média é {soma/len(numeros)}")
