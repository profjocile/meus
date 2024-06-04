'''
João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. 
Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida.
 Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!
'''

class bicicleta:
    def __init__(self, nome, modelo, cor, valor, vendida=False):
        self.nome = nome
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
        self.vendida = vendida
    
    def buzinar(self):
        print('Piii')

    def parar(self):
        print(f'A bicicleta {self.nome} esta correndo!')
    
    def correr(self):
        print(f'A bicicleta {self.nome} parou!')
    
    def compra(self):
        if self.vendida : print(f'A bicicleta {self.nome} foi vendida')
        else: print(f'A bicicleta {self.nome} não foi vendida')

bicicleta1 = bicicleta('Barra circular', 'Monark', 'Vermelha', 250, True)
bicicleta2 = bicicleta('Magrela', 'Caloi', 'Preta', 500)

bicicleta1.buzinar()
bicicleta1.correr()
bicicleta1.parar()
bicicleta1.compra()

bicicleta2.buzinar()
bicicleta2.correr()
bicicleta2.parar()
bicicleta2.compra()
