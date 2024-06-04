# criação de fuções de retorno

def imprimir_cabecalho():
    print('*'*26)
    print('*    Linguagem Python    *')
    print('*'*26)

def contar(inicio, fim):
    for a in range(inicio, fim+1):
        print(a, end=' ')

def imprimir(texto):
    print(texto)

imprimir_cabecalho()
print()
imprimir('Capítulo 7')
print()
contar(1,10)

