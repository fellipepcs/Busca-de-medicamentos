import requests
from bs4 import BeautifulSoup
from rest_framework.exceptions import NotFound


def get_medicamentos(medicamento):
    lista_medicamentos = []

    url_base = 'https://www.drogasil.com.br/search?w='
    response = requests.get(url_base + medicamento)

    site = BeautifulSoup(response.text, 'html.parser')

    medicamentos = site.findAll('div', attrs={'class': 'rd-col-8 rd-col-sm-4'})

    for remedio in medicamentos:
        nome_medicamento = remedio.find('h2', attrs={
                                        'class': 'ProductCardNamestyles__ProductNameStyles-sc-1l5s4fj-0 cuGHOR product-card-name'})
        site_redirect = remedio.find(
            'a', attrs={'class': 'LinkNextstyles__LinkNextStyles-t73o01-0 cpRdBZ LinkNext'})
        lista_medicamentos.append(
            {'Nome': nome_medicamento.text, 'link': site_redirect['href']})

    if lista_medicamentos == []:
        raise NotFound('Não possui medicamentos com o nome informado')

    return lista_medicamentos
