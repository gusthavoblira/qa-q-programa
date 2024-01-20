import random
contador=0
while True:
    num = random.randint(1,100)
    op=input('Digite a operação desejada:\n1-Jogar\n2-Ver pontuação\n\
3-Zerar pontuação\n4-Sair\nOpção: ')
    
    if op == '1':
        print(f'Shhh a resposta é {num}, mas não conta pra ninguém')
        tentativa=7
        while True:
            resposta=input('Adivinhe o número entre 1 a 100: ')
            resposta=int(resposta)
            if tentativa == 1:
                print('Você utilizou todas suas tentativas e não acertou o número gerado.\
 Tente outra vez.')
                break
            elif resposta == num:
                print(f'Parabéns, você acertou com {tentativa} tentativas restante(s)\n')
                contador += 1
                break
            else:
                tentativa -= 1
                if resposta > num:
                    print(f'Você errou, o número que você digitou \
é maior que o número gerado. Ainda restam {tentativa} tentativa(s).')
                elif resposta < num:
                    print(f'Você errou, o número que você digitou \
é menor que o número gerado. Ainda restam {tentativa} tentativa(s).')
            
    elif op == '2':
        print(f'Sua pontuação é: {contador} ponto(s).')
    
    elif op == '3':
       contador = 0 
       print(f'Sua pontuação foi zerada!')
    
    elif op == '4':
        print("\nObrigado por jogar, até logo!\n")
        break
    
    else:
        print("\nOpção inválida!\n")