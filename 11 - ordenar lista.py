lista=[]
while True: 
    op=input('Digite \'a\' para adicionar um novo número\
 ou \'o\' para ordenar a lista dada: ')          
    if op == 'a':
        num=input('Digite o número: ')
        num=int(num)
        lista.append(num)
    elif op == 'o':
        lista_ordenada = sorted(lista)
        print(f'Sua lista ordenada: {lista_ordenada}')
        break