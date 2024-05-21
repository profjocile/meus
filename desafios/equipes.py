'''
Faça um algoritmo para cadastrar os alunos que estão se canditando para equipes de desenvolvimento
'''

# Monte 4 equipes de alunos
equipe = [[],[],[],[]]

# Lista de nomes de alunos

nomes = set (['Caio','Davi', 'Edmilson', 'Erick', 'Esmael', 'Alison', 'Expedito', 'Armando', 'Kauã', 'Marcos', 'Graziel', 'Raiane', 'Natanael', 'Gabriel', 'Pedro', 'Silas'])

for j in range(4):
  for i in range(4): 
    equipe[i].append(nomes.pop())

# Mostre os nomes por cada equipe
for i in range(4): 
  print(f'Equipe {i + 1}: {equipe[i]}\n')