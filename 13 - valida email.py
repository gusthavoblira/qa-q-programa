import re  # Importa o módulo de expressões regulares

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(padrao, email):
        return True 
    else:
        return False

email = input("Digite um e-mail: ")

if validar_email(email):
    print("E-mail válido")
else:
    print("E-mail inválido")