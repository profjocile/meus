saldo = 2000.0
cheque_especial = 500
opcao1 = 10

while opcao1 != 0:
    opcao1 = int(input('Escolha a opção:\n[1] normal \n[2] universitária \n[0] Sair'))
    conta_normal = True if opcao1 == 1 else False

    if conta_normal :
        opcao2 = int(input('Escolha \n[1] para saque \n[2] Extrato '))
        if opcao2 == 1:
            saque = float(input('Valor do saque ='))
            if saldo >= saque: print('Realizado saque!')
            elif saldo + cheque_especial >= saque: print('Realizado saque usando o crédito!')
            else : print('Saldo e crédito insuficiente!')
        if opcao2 == 2: print('Extrato exibido!')

    elif opcao1 == 2:
        opcao2 = int(input('Escolha \n[1] para saque \n[2] Extrato '))
        if opcao2 == 1:
            saque = float(input('Valor do saque ='))
            if saldo >= saque: print('Realizado saque!')
            else: print('Saldo insuficiente')
        if opcao2 == 2:
            print('Extrato exibido!')

    else:
        print('Opção inválida!')

print('Opção 0 digitada! Obrigado e tchau!')