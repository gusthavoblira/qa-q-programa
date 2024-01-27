import random
lista = ["loja", "hoje","igreja","bola","face"]

palavra = random.choice(lista)
resposta_usuario = []
chutes = []
tentativa=10
tentativa=int(tentativa)
x = []

print(f'Não conta pra ninguém, mas a resposta é {palavra}')
for i in palavra:
		x.append(i)

while(True):
	x.sort()
	y = resposta_usuario
	y.sort()
	if x == y:
		print('Parabéns, você ganhou!')
		break
	letra = input("Escolha uma letra: ")
	if tentativa == 1:
		print('Você utilizou todas suas tentativas e não acertou a palavra gerada.\
Tente outra vez.')
		break
	if letra in chutes:
		print('Letra já utilizada, tente novamente!')
	elif letra in palavra:
		resposta_usuario.append(letra)
		chutes.append(letra)
		print('Essa letra está na palavra!')
		print(resposta_usuario)
	elif letra not in palavra:
		chutes.append(letra)
		tentativa -= 1
		print(f'Essa letra não está na palavra! Ainda restam {tentativa} tentativa(s)')