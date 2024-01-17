valor=input('Digite o valor desejado: ')
valor=float(valor)
op=input('Digite a operação desejada:\n 1 - Quilômetros para Milhas\n 2 - Milhas para Quilômetros\n\
 3 - Metros para Pés\n 4 - Pés para Metros\n 5 - Graus Celsius para Fahrenheit\n\
 6 - Graus Fahrenheit para Celsius\nDigite a opção desejada:')

if op == '1':
    resultado = valor*0.621371
    print(f'O resultado da conversão é: {resultado}')
    
elif op =='2':
    resultado = valor*1.60934
    print(f'O resultado da conversão é: {resultado}')

elif op == '3':
    resultado = valor*3.28084
    print(f'O resultado da conversão é: {resultado}')

elif op == '4':
    resultado = valor*0.3048
    print(f'O resultado da conversão é: {resultado}')

elif op == '5':
    resultado = (valor *9/5) + 32
    print(f'O resultado da conversão é: {resultado}')

elif op == '6':
    resultado = (valor - 32) / 1.8
    print(f'O resultado da conversão é: {resultado}')

else:
    print('Opção inválida, tente novamente')