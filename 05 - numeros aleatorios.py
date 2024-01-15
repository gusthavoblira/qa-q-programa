import random
numeros = []
i = 1

while i < 7:
    y = random.randint(1, 60)
    if y in numeros:
        random.randint(1, 60)               
    else:
        numeros.append(y)
    i += 1
tamanho = len(numeros)
if tamanho != 6: #ainda sim corre um pequeno risco, a solucao dele é de fato melhor
    random.randint(1, 60) 
    numeros.append(y)
    print(numeros)
else:
    print(numeros)





#Solucao dele:
#import random  # Importa o módulo random
# Inicializa uma lista vazia para armazenar os números
#numeros_megasena = []
# Gera 6 números aleatórios
#while len(numeros_megasena) < 6:
#    numero = random.randint(1, 60)  # Gera um número aleatório entre 1 e 60
#    if numero not in numeros_megasena:  # Verifica se o número já está na lista
#       numeros_megasena.append(numero)  # Adiciona o número à lista se ele ainda não estiver presente
#
#print("Números da Mega-Sena:", numeros_megasena)  # Imprime a lista de números
