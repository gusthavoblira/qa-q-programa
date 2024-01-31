pontos = 0
#print('''Escolha entre essas opções: 
#1 - Quiz fácil  
#4 - Sair''')

while True:
    #op=input('Digite opção desejada: \n')
    #if op == '1':
    print('''Qual a montanha mais alta do mundo?: 
a) Monte Chimborazo  
b) Monte Everest
c) Pico da Neblina
''')
    resposta=input('Digite sua resposta: ')
    if resposta == 'b':
            pontos += 1
            print(f'Acertou! Você ganhou um ponto, e sua pontuação agora é de {pontos} ponto(s)')
    else:
          print(f'Errou! Sua pontuação ainda está zerada')
    
    print('''Que país tem o formato de uma bota?: 
a) Itália 
b) Chile
c) Alemanha
''')
    resposta2=input('Digite sua resposta: ')
    if resposta2 == 'a':
            pontos += 1
            print(f'Acertou! Você ganhou um ponto, e sua pontuação agora é de {pontos} ponto(s)')
    elif resposta2 !='a':
        if pontos > 0:
            pontos -= 1
            print(f'Errou! Você perdeu um ponto e agora sua pontuação é de {pontos} ponto(s)')
        else:
            print('Você ainda não acertou e sua pontuação permanece zerada!')

    print('''Quantos ossos temos no nosso corpo?: 
a) 126 
b) 300
c) 206
''')
    resposta3=input('Digite sua resposta: ')
    if resposta3 == 'c':
            pontos += 1
            print(f'Acertou! Você ganhou um ponto, e sua pontuação agora é de {pontos} ponto(s)')
    elif resposta3 !='c':
        if pontos > 0:
            pontos -= 1
            print(f'Errou! Você perdeu um ponto e agora sua pontuação é de {pontos} ponto(s)')
        else:
            print('Você ainda não acertou e sua pontuação permanece zerada!')

    print(f'O jogo acabou, sua pontuação final é de {pontos} pontos!')
    break