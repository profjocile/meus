"""
Escreva um programa que peça ao usuário para digitar um número inteiro
 e verifique se ele é um número primo.
"""


numero = int(input("Digite um número inteiro: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break
if primo:
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")