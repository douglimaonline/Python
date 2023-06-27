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

# import pandas as pd

# # Definir a tabela como um DataFrame do pandas
# tabela = pd.DataFrame({
#     'Posição': list(range(1, 51)),
#     'Nome de usuário': ['@instagram', '@cristiano', '@leomessi', '@selenagomez', '@kyliejenner', '@therock',
#                         '@arianagrande', '@kimkardashian', '@beyonce', '@khloekardashian', '@nike', '@justinbieber',
#                         '@kendalljenner', '@natgeo', '@taylorswift', '@virat.kohli', '@jlo', '@kourtneykardash',
#                         '@nickiminaj', '@mileycyrus', '@neymarjr', '@katyperry', '@zendaya', '@kevinhart4real',
#                         '@iamcardib', '@ddlovato', '@kingjames', '@badgalriri', '@chrisbrownofficial', '@realmadrid',
#                         '@ellendegeneres', '@champagnepapi', '@fcbarcelona', '@billieeilish', '@championsleague',
#                         '@k.mbappe', '@gal_gadot', '@vindiesel', '@lalalalisa_m', '@nasa', '@dualipa', '@priyankachopra',
#                         '@shakira', '@nba', '@shraddhakapoor', '@snoopdogg', '@davidbeckham', '@khaby00', '@gigihadid',
#                         '@victoriassecret'],
#     'Profissão/Atividade': ['Rede social', 'Futebolista', 'Futebolista', 'Cantora, atriz e empresária',
#                             'Personalidade da televisão, modelo e empresária', 'Ator e ex-lutador profissional',
#                             'Cantora e atriz', 'Personalidade da televisão, modelo e empresária', 'Cantora',
#                             'Personalidade da televisão e modelo', 'Empresa esportiva multinacional', 'Cantor',
#                             'Cantora, Personalidade de televisão e Modelo', 'Revista', 'Cantora', 'Jogador de críquete',
#                             'Cantora, atriz e empresária', 'Personalidade da televisão e modelo', 'Cantora',
#                             'Cantora e atriz', 'Futebolista', 'Cantora', 'Atriz e cantora', 'Humorista e ator',
#                             'Rapper e atriz', 'Cantora e atriz', 'Basquetebolista', 'Cantora e empresária', 'Cantor',
#                             'Clube de futebol', 'Humorista e personalidade da televisão', 'Cantor', 'Clube de futebol',
#                             'Cantora', 'Competição entre clubes de futebol', 'Futebolista', 'Atriz', 'Ator',
#                             'Rapper e Dançarina', 'Agência espacial', 'Cantora', 'Atriz e cantora', 'Cantora',
#                             'Associação Nacional de Basquetebol', 'Atriz', 'Cantor',
#                             'Ex-futebolista Presidente do Inter Miami', 'Celebridade da Internet', 'Modelo',
#                             'Marca de lingerie'],
#     'País': ['Estados Unidos', 'Portugal', 'Argentina', 'Estados Unidos', 'Estados Unidos', 'Estados Unidos',
#              'Estados Unidos', 'Estados Unidos', 'Estados Unidos', 'Estados Unidos', 'Canadá', 'Estados Unidos',
#              'Estados Unidos', 'Estados Unidos', 'Índia', 'Estados Unidos', 'Estados Unidos', 'Trinidad e Tobago',
#              'Estados Unidos', 'Estados Unidos', 'Brasil', 'Estados Unidos', 'Estados Unidos', 'Estados Unidos',
#              'Estados Unidos', 'Estados Unidos', 'Estados Unidos', 'Barbados', 'Estados Unidos', 'Espanha',
#              'Estados Unidos', 'Canadá', 'Espanha', 'Estados Unidos', 'França', 'Israel', 'Estados Unidos',
#              'Tailândia', 'Estados Unidos', 'Reino Unido', 'Índia', 'Colômbia', 'Estados Unidos', 'Índia',
#              'Estados Unidos', 'Reino Unido', 'Senegal', 'Estados Unidos']
# })

# # Converter o DataFrame em um dicionário
# dados = []
# for _, row in tabela.iterrows():
#     dicionario = {
#         'name': row['Nome de usuário'].lstrip('@'),
#         'follower_count': row['Posição'],
#         'description': row['Profissão/Atividade'],
#         'country': row['País']
#     }
#     dados.append(dicionario)

# # Exibir o dicionário resultante
# for item in dados:
#     print(item)


