'''
Faça um algoritmo para cadastrar os alunos que estão se canditando para equipes de desenvolvimento
'''

# Monte 4 equipes de alunos
equipe = [[],[],[],[]]
global nomes


# Lista de nomes de alunos
nomes = set()

def criar_lista(nomes):
  nomes2 = nomes.copy()
  for j in range(4):
    for i in range(4): 
      equipe[i].append(nomes2.pop())
  return equipe

# Mostre os nomes por cada equipe
def mostrar():
  for i in range(4): 
    print(f'Equipe {i + 1}: {equipe[i]}\n')

criar_lista(['Caio','Davi', 'Edmilson', 'Erick', 'Esmael', 'Alison', 'Expedito', 'Armando', 'Kauã', 'Marcos', 'Graziel', 'Raiane', 'Natanael', 'Gabriel', 'Pedro', 'Silas'])
mostrar()