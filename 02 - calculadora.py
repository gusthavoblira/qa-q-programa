primeiro_num=input("Digite o primeiro número:")
primeiro_num=float(primeiro_num)
op=input("Digite a operação desejada (+ para soma, - para subtração, * para multiplicação, / para divisão): ")
segundo_num=input("Digite o segundo número:")
segundo_num=float(segundo_num)

if op == '+':
    soma=primeiro_num + segundo_num
    soma=float(soma)
    print(f'Resultado da soma é: {soma}')

elif op == '-':
    sub=primeiro_num - segundo_num
    sub=float(sub)
    print(f'Resultado da subtração é: {sub}')

elif op == '*':
    mult=primeiro_num * segundo_num
    mult=float(mult)
    print(f'Resultado da multiplicação é: {mult}')

elif op == '/':
    if segundo_num == 0:
        print('Divisão por 0 não é permitida!')
    else:
        divisao=primeiro_num / segundo_num
        divisao=float(divisao)
        print(f'Resultado da divisão é: {divisao}')  

else:
    print(f"Operação inválida, tente novamente!")