import pandas as pd

print('''Escolha entre essas opções: 
1 - Adicionar Despesa  
2 - Ver todas despesas
3 - Filtrar por categoria
4 - Filtrar por data
5. Sair''')

while(True):
	op = int(input("Escolha um número: "))
	if(op == 1):
		valor = float(input('Digite o valor: '))
		descricao = input('Digite a descrição: ')
		categoria = input('Digite a categoria: ')
		data = input('Digite a data: ')
		despesa_df = {'Valor': [valor],
        'desc': [descricao],
        'cat': [categoria],
		'data': [data]
        }
		df = pd.DataFrame(despesa_df)
		df.to_csv('despesas.csv', index=False, mode='a',header=False)
		print('Despesa adicionada com sucesso!')
		
	elif(op==2):
		df = pd.read_csv('despesas.csv')
		print(df.to_string())
		Total = df['Valor'].sum()
		print(f'\nA soma das despesas é: {Total} reais\n')
	elif(op==3):
		usuario_cat = input('Qual categoria quer buscar?: ')
		df = pd.read_csv("despesas.csv", sep = ",")
		result = df[df['cat']==usuario_cat]
		if usuario_cat not in result.values:
			print('Categoria não encontrada!')
		else:
			print(result)
		Total_cat = result['Valor'].sum()	
		print(f'\nA soma das despesas é: {Total_cat} reais\n')
	elif(op==4):
		data_cat = input('Qual data quer buscar?: ')
		df = pd.read_csv("despesas.csv", sep = ",")
		result = df[df['dat']==data_cat]
		if data_cat not in result.values:
			print('Data não encontrada!')
		else:
			print(result)
			Total_data = result['Valor'].sum()	
			print(f'\nA soma das despesas é: {Total_data} reais\n')
	elif(op == 5):
		break		
	else:
		print("Escolha uma opção válida")
		

#Planeje a estrutura de dados que será usada para armazenar as despesas, incluindo informações como valor, descrição, categoria e data.

#Implemente um menu de opções intuitivo para o usuário,
#permitindo que ele escolha entre registrar uma nova despesa, visualizar um resumo por categoria,
#visualizar o total de despesas ao escolher uma data e sair do programa.

#Utilize loops para permitir que o usuário continue interagindo com o programa até que escolha sair.
#Implemente a lógica para calcular os totais de despesas por categoria e por data, usando listas e dicionários para organizar os dados.
#Considere a persistência de dados, como salvar as despesas em um arquivo CSV, para que as informações
#sejam mantidas entre as execuções do programa.