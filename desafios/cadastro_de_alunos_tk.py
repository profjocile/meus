# Cadastrar os dados dos alunos
import tkinter as tk

def cadastrar_aluno():    
    nome = entry_nome.get  # input('Nome do aluno: ')
    #endereco = input('Endereço do aluno: ')
    #turma = input('Turma do aluno: ')
    aluno = {
        'nome': nome,
        #'endereco' : endereco,
        #'turma' : turma
    }
    alunos.append(aluno)
    print(f'Aluno {nome} cadastrado!')
    entry_nome.delete(0, tk.END)
        

def imprimir_alunos():
    print('Lista de alunos:')
    for aluno in alunos:
        print(aluno)

alunos = []
janela = tk.Tk()
janela.title('Cadastro de alunos')

label_nome = tk.Label(janela, text='Nome')
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

botao_cadastar = tk.Button(janela, text='Cadastrar', command=cadastrar_aluno)
botao_cadastar.pack()

janela.mainloop()

# cadastrar_aluno()
# imprimir_alunos()
