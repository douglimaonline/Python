import random

import pandas as pd

# data = pd.read_html('https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o')[0]
data = pd.read_html('https://pt.wikipedia.org/wiki/Lista_das_contas_mais_seguidas_no_Instagram')[0]

df = data.to_dict('records')

class Celebrity:
    def __init__(self, c_position, c_user, c_name, c_followers, c_description, c_country):
        self.position = c_position
        self.user = c_user
        self.name = c_name
        self.followers = c_followers
        self.description = c_description
        self.country = c_country

celebrities = []
for data in range(0, len(df)):
    celebrity = Celebrity(df[data]['Posição'], df[data]['Nome de usuário'],
                          df[data]['Proprietário/a'], df[data]['Seguidores[2] (milhões)*'],
                          df[data]['Profissão/Atividade'], df[data]['País'])
    celebrities.append(celebrity)


class Game:
    def select_celebrity(self, celebrities_list):
        sel_celebrity = random.choice(celebrities_list)
        return sel_celebrity

game = Game()

print(game.select_celebrity(celebrities).name)