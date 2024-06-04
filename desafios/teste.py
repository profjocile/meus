# Exemplo para verificar palíndromo

#if string == string[::-1]:
#    print("É", end='')
#else:
#    print("Não", end='')
#print(' um palíndromo.')

string = input("Digite uma string: ")
resultado = 'é' if string == string[::-1] else'não é'
print(f'{string} {resultado} um palíndromo.')