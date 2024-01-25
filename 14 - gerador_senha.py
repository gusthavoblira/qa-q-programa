import string
import random

tamanho = int(input("Tamanho da senha: "))

print('''Escolha entre essas opções: 
		1. Números
		2. Letras
		3. Caracteres especiais
		4. Sair''')

lista_caracteres = ""

while(True):
	op = int(input("Escolha um número: "))
	if(op == 1):
		lista_caracteres += string.ascii_letters
	elif(op == 2):
		lista_caracteres += string.digits
	elif(op == 3):
		lista_caracteres += string.punctuation
	elif(op == 4):
		break
	else:
		print("Escolha uma opção válida")

senha = []

for i in range(tamanho):
	randomchar = random.op(lista_caracteres)
	senha.append(randomchar)

print("Sua senha é:" + "".join(senha))
