'''
Faça um algoritmo para cadastrar os alunos que estão se canditando para equipes de desenvolvimento
'''

# Monte 4 equipes de alunos
equipe1 = []
equipe2 = []
equipe3 = []
equipe4 = []

# Lista de nomes de alunos

nomes = set (['Caio','Davi', 'Edmilson', 'Erick', 'Esmael', 'Alison', 'Expedito', 'Armando', 'Kauã', 'Marcos', 'Graziel', 'Raiane', 'Natanael', 'Gabriel', 'Pedro', 'Silas'])

for i in range(4):
    equipe1.append(nomes.pop())
    equipe2.append(nomes.pop())
    equipe3.append(nomes.pop())
    equipe4.append(nomes.pop())

# Mostre os nomes por cada equipe
print(f'''
      Equipe 1: {equipe1}\n
      Equipe 2: {equipe2}\n
      Equipe 3: {equipe3}\n
      Equipe 4: {equipe4}\n
      ''')
