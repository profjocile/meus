# Exemplo para verificar palíndromo

string = input("Digite uma string: ")
resultado = 'é' if string == string[::-1] else'não é'
print(f'{string} {resultado} um palíndromo.')