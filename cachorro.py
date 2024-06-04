class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        if self.acordado:
            print(f'{self.nome} está latindo')
        else:
            print(f'{self.nome} não está acordado')

    def comer(self):
        print(f'{self.nome} está comendo')
    
    def dormir(self):
        if self.acordado:
            print(f'{self.nome} está acordado')
        else: print(f'{self.nome} está dormindo')

cao_1 = Cachorro('Totó', 'Caramelo', False)
cao_2 = Cachorro('Dog', 'Branco')
cao_3 = Cachorro('Chiaua', 'Marrom')

cao_1.latir()
cao_1.comer()
cao_1.dormir()
cao_1.acordado = True
cao_1.dormir()

cao_2.latir()
cao_2.comer()
cao_2.dormir()

cao_3.latir()
cao_3.comer()
cao_3.dormir()