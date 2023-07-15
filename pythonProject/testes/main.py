import pandas as pd
from state_class import States
import random

tabelas = pd.read_html('https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil')[1]
tabelas = tabelas.fillna('')
dict_table = tabelas.to_dict('records')


lista_estados = []
for row in range(0, len(dict_table)):
    state = States(dict_table[row]['Unidade federativa'], dict_table[row]['Abreviação'],
                   dict_table[row]['Sede de governo'], dict_table[row]['Área (km²)'],
                   dict_table[row]['População (2014)'], dict_table[row]['Densidade (2005)'],
                   dict_table[row]['PIB (2015)'], dict_table[row]['(% total) (2015)'],
                   dict_table[row]['PIB per capita (R$) (2015)'], dict_table[row]['IDH (2010)'],
                   dict_table[row]['Alfabetização (2016)'], dict_table[row]['Mortalidade infantil (2016)'],
                   dict_table[row]['Expectativa de vida (2016)'])
    lista_estados.append(state)

print(lista_estados[7].uf)
print(lista_estados[7].idh)