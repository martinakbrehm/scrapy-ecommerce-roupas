#import requests
import requests
from bs4 import BeautifulSoup


url = 'https://www.tng.com.br'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_='prateleira n12colunas')


    # Imprima os nomes dos produtos encontrados
    #for product in products:
       # print(product_name.text)
else:
    print('Falha ao acessar a página:', response.status_code)

