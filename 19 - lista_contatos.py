contato =[]

print('''Escolha entre essas opções: 
1 - Adicionar contato  
2 - Listar contatos
3 - Buscar contato
4 - Excluir contato
5. Sair''')

while True:
    op = input('Digite a opção desejada: ')
    if op == '1':
        nome=input('Digite o nome do contato: ')
        telefone=input('Digite o telefone do contato: ')
        email=input('Digite o email do contato: ')

        contato_dic = {
        "Nome": nome,
        "Telefone": telefone,
        "Email": email
        }
        contato.append(contato_dic)
    elif op == '2':
        for contato_dic in contato:
            print(f"\nNome: {contato_dic['Nome']}")
            print(f"Telefone: {contato_dic['Telefone']}")
            print(f"E-mail: {contato_dic['Email']}\n")
    elif op =='3':
        busca_nome=input('Digite o nome do contato a ser buscado: ')
        for contato_dic in contato:
            if contato_dic["Nome"] != busca_nome:
                print('Não encontrado!')
            else:
                print(f"\nNome: {contato_dic['Nome']}")
                print(f"Telefone: {contato_dic['Telefone']}")
                print(f"E-mail: {contato_dic['Email']}\n")
            break
    elif op=='4':
        exclusao_contato=input('Digite o nome do contato a ser excluído: ')
        for contato_dic in contato:
            if contato_dic["Nome"] == exclusao_contato:
                contato.remove(contato_dic)
                break
            else:
                print('Não encontrado!')
    elif op == '5':
        break