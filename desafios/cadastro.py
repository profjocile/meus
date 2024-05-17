'''
Faça um algoritmo para cadastrar os alunos que estão cursando as disciplinas Matemática I e Contabilidade I. Essas disciplinas aceitam 150 e 100 alunos respectivamente. O cadastro deve ser feito pelos números de matrícula dos alunos. Feito o cadastro, indique qual ou quais alunos estão cursando as duas disciplinas
'''
mat1 = set()
cont1 = set()
ambos = []

while len(mat1) < 5: # 150
    matricula = int(input("Digite a matrícula do aluno de Matemática I: "))
    mat1.add(matricula)

while len(cont1) < 5: # 100
    matricula = int(input("Digite a matrícula do aluno de Contabilidade I: "))
    cont1.add(matricula)

for aluno in mat1.intersection(cont1):
    ambos.append(aluno)

print("Alunos cursando ambas as disciplinas:")
for aluno in ambos:
    print(aluno)
