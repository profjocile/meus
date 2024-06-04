# Cadastrar os dados dos alunos

def cadastrar_aluno():    
    while True:
        nome = input('Nome do aluno: ')
        endereco = input('Endereço do aluno: ')
        turma = input('Turma do aluno: ')
        aluno = {
            'nome': nome,
            'endereco' : endereco,
            'turma' : turma
        }
        alunos.append(aluno)
        print(f'Aluno {nome} cadastrado!')
        continuar = input('Cadastar outro? (s/n):')
        if continuar == 'n': break

def imprimir_alunos():
    print('Lista de alunos:')
    for aluno in alunos:
        print(aluno)

alunos = []
cadastrar_aluno()
imprimir_alunos()
