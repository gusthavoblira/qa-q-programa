import random
contador=0
while True:
    num = random.randint(1,100)
    op=input('Digite a operação desejada:\n1-Jogar\n2-Ver pontuação\n\
3-Zerar pontuação\n4-Sair\nOpção: ')
    
    if op == '1':
        print(num)
        resposta=input('Digite sua resposta("Primo" ou "Não primo"): ')
        for i in range(2, num):
            if (num % i) == 0:
                valida_primo="Não primo"
                break
            else:
                valida_primo="Primo"
        if resposta == valida_primo:
             print('Acertou!')
             contador += 1
        else:
            print(num)
            print('Perdeu tudo, tente novamente!')
            contador = 0
    
    elif op == '2':
        print(f'Sua pontuação é {contador} ponto(s)')
    
    elif op == '3':
       contador = 0 
       print(f'Sua pontuação foi zerada!')
    
    elif op == '4':
        print("\nAté logo!\n")
        break
    
    else:
        print("\nOpção inválida.\n")