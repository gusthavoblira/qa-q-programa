frase=input('Digite a frase desejada: ').lower()
freq={}
count = 0
for i in frase:
    if i.isalpha():
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
print(f'Caracteres da frase: {freq}')
