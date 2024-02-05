import time

print("Escolha o modo:\n1 - Temporizador\n2 - Regressivo")
op = input("Digite 1 ou 2: ")

tempo = int(input("Digite o tempo (em segundos): "))

if op == '1':
    contador = 0
    while contador < tempo:
        print(contador + 1, end='\r')
        time.sleep(1)
        contador += 1
elif op == '2':
    while tempo > 0:
        print(tempo, end='\r')
        time.sleep(1)
        tempo -= 1
else:
    print("Escolha inválida.")

print(' ' * 10, end='\r')
print("\nTempo esgotado!")