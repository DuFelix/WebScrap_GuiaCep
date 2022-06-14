from email import header
from wsgiref import headers
import requests
from bs4 import BeautifulSoup

url = 'https://cep.guiamais.com.br/busca/sao+paulo-sp?page=1'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ApplewebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
}

