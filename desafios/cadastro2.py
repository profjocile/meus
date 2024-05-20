'''
Faça um algoritmo para cadastrar os alunos que estão cursando as disciplinas Matemática I e Contabilidade I. Essas disciplinas aceitam 150 e 100 alunos respectivamente. O cadastro deve ser feito pelos números de matrícula dos alunos. Feito o cadastro, indique qual ou quais alunos estão cursando as duas disciplinas

1. Criar listas de:
  1.1. matematica1
  1.2. contabilidade1
'''
matematica1 = []
contabilidade1 = []
'''
3. Cadastrar os alunos por disciplina
  3.1 Criar uma repetição até no máximo de 150 para a lista de matemática1
'''
lista = 0
while lista<150:
  numero = (int(input('Entre com o num. da matr. para Matemática1, ou 0 pra sair: ')))
  if numero == 0: break
  lista = lista + 1
  matematica1.append(numero)
  
print('As matrículas na Matematica 1 são: ', matematica1)
print('-'*40)

while lista<100:
  numero = (int(input('Entre com o num. da matr. para Contabilidade1, ou 0 pra sair: ')))
  if numero == 0: break
  lista = lista + 1
  contabilidade1.append(numero)

print('As matrículas na Contabilidade 1 são: ', contabilidade1)
print('-'*40)

''' Solução usando conjuntos:
conjunto_mat = set(matematica1)
conjunto_cont = set(contabilidade1)
resultado = conjunto_mat.intersection(conjunto_cont)
'''

# Solução usando loop for
resultado = []
for num1 in matematica1:
  for num2 in contabilidade1:
    if num1 == num2 : resultado.append(num1)

print('As matrículas que estão nas duas disciplinas são: ', resultado)
