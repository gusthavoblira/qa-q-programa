frase=input("Digite sua frase: ")
x = frase.split()
count = 0
for item in x:
    count += 1
if count !=1:
    print(f'O texto contém {count} palavras.')
else:
    print(f'O texto contém 1 palavra.')