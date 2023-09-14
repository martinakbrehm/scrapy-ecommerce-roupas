import requests
import json
from bs4 import BeautifulSoup

product_url = 'https://www.hering.com.br/camiseta-masculina-gola-v-basicos-do-brasil-4k20nmcen/p'

response = requests.get(product_url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    item_list = []

    title = soup.find('h1', class_='hering-hering-components-3-x-product-content--name').text

    price_elements = soup.find('span', class_='hering-hering-components-3-x-currencyContainer')

    if price_elements:
        price = price_elements.find_all('span')
        price_text = ''.join(span.text for span in price)

    else: 
        print('elemento de preço não encontrado')

    description = soup.find('div', class_='hering-hering-components-3-x-productDescriptionValue').text

    item_info = {
        'title': title,
        'price': price_text,
        'description': description,
        'url': product_url,
    }
    item_list.append(item_info)
    print(item_info)
else:
    print('Falha ao acessar a página:', response.status_code)

output_file = 'products.json'

with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(item_list, json_file, ensure_ascii=False, indent=4)

print(f'\nDados salvos no arquivo {output_file}')
