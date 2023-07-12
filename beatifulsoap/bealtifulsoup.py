import os
import requests
from bs4 import BeautifulSoup
import pandas as pd



site_info = requests.get('https://pt.wikipedia.org/wiki/Lista_das_contas_mais_seguidas_no_Instagram')

content = site_info.content

site = BeautifulSoup(content, 'html.parser')

os.system('cls')

contas = site.find(name='table')
contas_str = str(contas)
pessoas = pd.read_html(contas_str)
print(pessoas)
