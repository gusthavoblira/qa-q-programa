tarefas = []
i = 0

while i < 4:
    op=input('Digite a operação desejada:\n1-Inserir tarefa\n2-Listar tarefas\n\
3-Remover tarefas\n4-Sair\nOpção: ')
    if op == '1':
        add_tarefa=input('Digite a tarefa desejada: ')
        tarefas.append(add_tarefa)
        print('Tarefa inserida com sucesso!\n')
    elif op == '2':
        if len(tarefas) == 0:
            print('Lista vazia!\n')
        else:
            print(f'Essas são suas tarefas:\n{tarefas}')
    elif op == '3':
        if len(tarefas) == 0:
            print('Lista vazia!\n')
        else:
            apagar=input('Digite o número da tarefa a ser excluída: ')
            apagar=int(apagar)
            tarefas.pop(apagar)
            print('Tarefa apagada com sucesso!\n')           
    elif op == '4':
        break
    else:
        print('Opção inválida, tente novamente!\n')

#TESTE 04: Teste situações em que o usuário tenta remover uma tarefa que não existe na lista.
