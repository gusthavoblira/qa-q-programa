import requests
import json

origem = input('Digite a moeda original: ')
destino =input('Digite a moda de destino: ')


base_url = "https://open.er-api.com/v6/latest/"
url = ''.join([base_url, origem])
response = requests.get(url)


while (True):
  try:
    valor_origem= float(input('Digite o valor: '))
  except:
    print('Digite um valor válido!')
    break
  if valor_origem <=0:
    print('Digite um valor maior que 0!')
    break
  try:
    resultado=response.json()['rates'][destino]
    resultado = float(resultado)
    conversao = valor_origem * resultado
    print(f'O resultado da conversão entre {origem} e {destino} é: {conversao} \
considerando a conversão que nesse momento está em {resultado}')
    break
  except:
    print('Moeda incorreta, tente novamente!')
    break


#conteudos uteis com json/consultas
#text = json.dumps(response.json(), sort_keys=True, indent=4)
#print(text)
#print(response.status_code)
#print(response.json())