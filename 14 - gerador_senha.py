import string
import random

tamanho = int(input("Tamanho da senha: "))

print('''Escolha entre essas opções: 
		1. Letras minúsculas
	        2. Letras maiúsculas
		3. Números
		4. Caracteres especiais
		5. Sair''')

lista_caracteres = ""

while(True):
	op = int(input("Escolha um número: "))
	if(op == 1):
		lista_caracteres += string.ascii_lowercase
	elif(op==2):
		lista_caracteres += string.ascii_uppercase
	elif(op == 3):
		lista_caracteres += string.digits
	elif(op == 4):
		lista_caracteres += string.punctuation
	elif(op == 5):
		break
	else:
		print("Escolha uma opção válida")

senha = []

for i in range(tamanho):
	randomchar = random.choice(lista_caracteres)
	senha.append(randomchar)

print("Sua senha é:" + "".join(senha))
