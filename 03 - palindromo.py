frase=input("Digite sua frase: ").lower()
remover = [",", " ", "!","?","-"]
for char in remover:
    frase = frase.replace(char,"")
frase_invertida=frase[::-1]
if frase_invertida == frase:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

#https://www.geeksforgeeks.org/string-slicing-in-python/ - documentação que eu usei para inverter a frase
