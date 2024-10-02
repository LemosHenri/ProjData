from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

import pandas as pd

driver = webdriver.Firefox()

URL = 'https://www.vivareal.com.br/venda/rj/volta-redonda/'
driver.get(URL)
soup = BeautifulSoup(driver.page_source, 'html.parser')

nome_data = []
area_data = []
quartos_data = []
banheiros_data = []
garagem_data = []
valor_data = []
endereco_data = []

for pag in range(50):

    produtos = soup.findAll('div', attrs = {'class': 'js-card-selector'}) 
    next = driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button')

    for prod in produtos:

        nome = prod.find('span', attrs = {'class': 'property-card__title js-cardLink js-card-title'})
        area = prod.find('span', attrs = {'class': 'property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area'})
        quartos = prod.find('span', attrs = {'class': 'property-card__detail-value js-property-card-value'})
        banheiros = prod.find('span', attrs = {'class': 'property-card__detail-value js-property-card-value'})
        garagem = prod.find('span', attrs = {'class': 'property-card__detail-value js-property-card-value'})
        preco = prod.find('div', attrs = {'class': 'property-card__price js-property-card-prices js-property-card__price-small'})
        endereco = prod.find('span', attrs = {'class': 'property-card__address'})

        nome_data.append(nome.text)
        area_data.append(area.text)
        quartos_data.append(quartos.text)
        banheiros_data.append(banheiros.text)
        garagem_data.append(garagem.text)
        valor_data.append(preco.text)
        endereco_data.append(endereco.text)
    
    next.click()


driver.quit()

# CRIAÇÃO DO DATA FRAME

dict = {
    'Titulo': nome_data,
    'Área': area_data,
    'Quartos': quartos_data,
    'Banheiros': banheiros_data,
    'Vaga Garagem': garagem_data,
    'Valor': valor_data,
    'Endereço': endereco_data,
}


df = pd.DataFrame(dict)

# ARMAZENAMENTO EM ARQUIVO .CSV
df.to_csv('planilha.csv', index = False)