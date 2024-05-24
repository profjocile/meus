# Exemplo para contar vogais e consoantes

vogais = 'aãeéioôóuAÃEÉIOU'
numeros = '0123456789'
soma_vogais = 0
soma_consoantes = 0
texto = input("Digite um texto: ")
espaco = 0
for letra in texto:
    if letra in vogais:
        soma_vogais +=1
    elif letra == ' ':
        espaco = espaco + 1
    elif letra in numeros:
        print(f'Você digitou: {letra}')
    else:
        soma_consoantes += 1
print(f"Vogais: {soma_vogais}\nConsoantes: {soma_consoantes} ")

#vogais = sum(1 for char in string if char in 'aeiouAEIOU')
#consoantes = sum(1 for char in string if char.isalpha() and char not in 'aeiouAEIOU')
#print(f"Vogais: {vogais}, Consoantes: {consoantes}")