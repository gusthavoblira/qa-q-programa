import csv

print('''Escolha entre essas opções: 
		1. Adicionar Livro  
	        2. Ver biblioteca
		3. Sair''')

while(True):
	op = int(input("Escolha um número: "))
	if(op == 1):
		livro = input('Digite o livro: ')
		autor = input('Digite o autor: ')
		ano = input('Digite o ano: ')
		f = open('biblioteca.csv', '+a', newline='', encoding='utf-8')
		w= csv.writer(f)
		w.writerow([livro,autor,ano])
		f.close()
	elif(op==2):
		with open('biblioteca.csv', newline='', encoding='utf-8') as g:
			reader=csv.reader(g)
			print('Livro|Autor|Ano')
			for row in reader:
				print("|".join(row))
	elif(op == 3):
		break		
	else:
		print("Escolha uma opção válida")

    #Certifique-se de criar um arquivo CSV vazio para armazenar os detalhes dos livros,
    #com as colunas apropriadas para título do livro, autor e ano de publicação.