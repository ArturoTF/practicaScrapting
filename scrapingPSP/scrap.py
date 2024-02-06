import requests
from bs4 import BeautifulSoup
import pandas as pd

"""
Este programa mediante la variable url que es una especie de diccionario clave-valor, voy scrapeando cada link, el primero
los items tops, el segundo moviles, el tercero tablets y el cuarto Laptops.
Mediante un doble bucle el primero va cogiendo de uno en uno una url y el segundo es el que scrapea el codigo mediante la clase
'col-md-4', 'col-xl-4', 'col-lg-4' y filtrando la clase title, price y name y los cojo y los guardo en productosResult y al final lo
convierto en un csv mediante el metodo to_csv.
"""
urls = {
    'Top items': 'https://webscraper.io/test-sites/e-commerce/allinone',
    'Moviles': 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch',
    'Tablets': 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets',
    'Laptops': 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
}

lista_productos = []

for category, url in urls.items():
    response = requests.get(url)
    data = response.text

    soup = BeautifulSoup(data, 'html.parser')

    for product_container in soup.find_all('div', class_=['col-md-4', 'col-xl-4', 'col-lg-4']):

        nombre = product_container.find('a', class_='title').text.strip()
        precio = product_container.find('h4', class_='price').text.strip()
        lista_productos.append({'Category': category, 'name': nombre, 'precio': precio})
productosResult = pd.DataFrame(lista_productos)

productosResult.to_csv('C:/Users/Arturo/Documents/scrapingPSP/productos.csv', index=False)
