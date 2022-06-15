from email import header
from sqlite3 import Row
from wsgiref import headers
from pyparsing import White
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://cep.guiamais.com.br/busca/sao+paulo-sp?page=1'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ApplewebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
placa = soup.find('table', class_='table s_table_box table-striped table-responsive')
linha = placa.find_all('tr')
ultima_pag = '1'

find_table = soup.find('table') 
rows = find_table.find_all('tr') 
for i in rows: 
    table_data = i.find_all('td') 
    data = [j.text for j in table_data] 
df = pd.DataFrame(data)
df.to_csv('teste.csv')