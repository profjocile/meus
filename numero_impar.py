'''
Escreva um programa que peça ao usuário para 
digitar um número inteiro positivo e 
calcule a soma de todos os números ímpares 
de 1 até esse número.
'''
numero = 1
while numero != 0:
    soma = 0
    numero = int(input('Informe o número (0 para sair): '))    
    if numero > 1:
        for i in range(1, numero):
            if i % 2 == 0:
                continue
            else:
                print (i, end='')
                soma += i
                if i < numero - 2 : print(' + ', end='')
        print(f' = {soma}')
    elif numero == 0 : break
    else:
        print('Número inválido, tem que ser inteiro e positivo!')
