while (True):
    op=input('Digite a operação desejada:\n1-Construir um select\n2-Construir um insert\n\
3-Construir um update\n4-Sair\nOpção: ')
    if op =='1':
        colunas_select=input('Digite as colunas separadas por vírgula: ')
        tabelas_select=input('Digite a(s) tabela(s) desejadas separadas por vírgula: ')
        where_op=input('Deseja Where? [S/N]: ')
        if where_op=='S':
            where=input('Digite a condição do where: ')
            resultado_select_where=print(f'Comando: SELECT {colunas_select} FROM {tabelas_select} WHERE {where}')
        else:
             resultado_select=print(f'Comando: SELECT {colunas_select} FROM {tabelas_select}')
    
    elif op=='2':
        colunas_insert=input('Digite as colunas separadas por vírgula: ')
        tabela_insert=input('Digite a tabela desejada: ')
        valores_insert=input('Digite os valores separados por vírgula: ')
        resultado_insert=print(f'INSERT INTO {tabela_insert} ({colunas_insert}) VALUES ({valores_insert})')
    
    elif op =='3':
        colunas_update=input('Digite as colunas separadas por vírgula com o valor para atualizar: ')
        tabela_update=input('Digite a tabela desejada: ')
        where_op=input('Deseja Where? [S/N]: ')
        if where_op=='S':
            where_up=input('Digite a condição do where: ')
            resultado_select_where=print(f'Comando: UPDATE {tabela_update} SET {colunas_update} WHERE {where_up}')
        else:
             resultado_select=print(f'Comando: UPDATE {tabela_update} SET {colunas_update}')
    
    elif op =='4':
        break

    else:
        print('Opção inválida!\n')

    
