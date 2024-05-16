numeros = input("Digite uma lista de números separados por vírgulas: ")
numeros = numeros.split(",")
maior = int(numeros[0])
for numero in numeros:
    if int(numero) > maior:
        maior = int(numero)
        # print(maior)
print("O maior número da lista é", maior)