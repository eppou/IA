import pandas as pd
import numpy as np
import networkx as nx
import itertools
import random
import dataTreatment as dt

weapond_df = pd.read_csv("DS3_weapon.csv")
boss_df = pd.read_csv("bosses_csv.csv")

weapond_df[['Physical damage','Magical damage','Fire damage','Lightning damage','Dark damage']] = weapond_df['Damage'].str.split('/',expand=True)
colunas_para_converter = ['Physical damage', 'Magical damage', 'Fire damage', 'Lightning damage', 'Dark damage']

# Itere pelas colunas e converta os valores em números
for coluna in colunas_para_converter:
    weapond_df[coluna] = pd.to_numeric(weapond_df[coluna], errors='coerce')

def Pontuacao(arma, chefe):
    dano_geral = arma['Physical damage']
    dano_magico_arma = arma['Magical damage']
    dano_fogo_arma = arma['Fire damage']
    dano_raio_arma = arma['Lightning damage']
    fraqueza_chefe = chefe['Fraqueza']
    resistencia_chefe = chefe['Resistente']
    veloz = chefe['Velocidade']
    peso_arma = arma['Weight']

    pontuacao = int(dano_geral)

    if fraqueza_chefe == 'magic':
        pontuacao += int(dano_magico_arma * 5)
    elif fraqueza_chefe == 'fire':
        pontuacao += int(dano_fogo_arma * 5)
    elif fraqueza_chefe == 'light':
        pontuacao += int(dano_raio_arma * 5)

    if resistencia_chefe == 'magic':
        pontuacao += int(dano_magico_arma * 0.25)
    elif resistencia_chefe == 'fire':
        pontuacao += int(dano_fogo_arma * 0.25)
    elif resistencia_chefe == 'light':
        pontuacao += int(dano_raio_arma * 0.25)

    if veloz == 1:
        pontuacao -= int(peso_arma * 8)
    elif veloz == 0:
        pontuacao -= int(peso_arma * 0.5)

    return pontuacao


def heuristic(weapon, boss):
    # Calcule uma estimativa do custo usando a pontuação da arma
    weapon_score = G[boss][weapon]['weight']
    return weapon_score

def real_cost(current_weapon, next_weapon):
    return G[current_weapon][next_weapon]['weight']

def astar_search(graph, start, goal, heuristic, real_cost):
    open_list = [(start, 0)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    while open_list:
        current, current_cost = min(open_list, key=lambda x: x[1])
        open_list.remove((current, current_cost))
        
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, current_cost
        
        for neighbor in graph.neighbors(current):
            custo_total = real_cost(current, neighbor)
            tentative_g_score = g_score[current] + custo_total
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = g_score[neighbor] + heuristic(neighbor, current)
                open_list.append((neighbor, f_score))
    
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
        path.reverse()
    return path, custo_total

def goal_weapon(boss, weapons_data):
    # Calcule a arma ideal para derrotar o chefe
    weapons = weapons_data.keys()
    best_weapon = None
    best_score = -1
    for weapon in weapons:
        score = Pontuacao(weapons_data[weapon], boss)
        if score > best_score:
            best_weapon = weapon
            best_score = score
    return best_weapon



numbem_boss = random.randint(0,21)
boss = boss_df.loc[numbem_boss]
G = nx.DiGraph()
G.add_node(boss['Nomes'])


# Crie um dicionário para mapear armas para seus dados
weapons_data = {row['Name']: row for index, row in weapond_df.iterrows()}

# Calcule as pontuações e adicione as arestas do boss para as armas
df_physical, df_lightning, df_fire, df_magic = dt.dataFrame_creator(weapond_df)


# Calcule as pontuações e adicione as arestas do chefe para armas aleatórias de cada DataFrame
for df_name, df in [("Physical", df_physical), ("Lightning", df_lightning), ("Fire", df_fire), ("Magic", df_magic)]:
    random_weapon = df.iloc[random.randint(0,9)]  # Escolha uma arma aleatória do DataFrame
    score = Pontuacao(random_weapon, boss)
    G.add_edge(boss['Nomes'], random_weapon['Name'], weight=score)

    for index, weapon_row in df.iterrows():
        if weapon_row['Name'] != random_weapon['Name']:
            # Calcule a pontuação para esta conexão (você pode ajustar a lógica conforme necessário)
            score = Pontuacao(weapon_row, boss)
            G.add_edge(random_weapon['Name'], weapon_row['Name'], weight=score)


goal = goal_weapon(boss, weapons_data)

best_weapon_path, custo = astar_search(G, boss['Nomes'], goal , heuristic, real_cost)
if best_weapon_path:
    best_weapon = best_weapon_path[-1]  # A última arma no caminho é a melhor
    print(f"A melhor arma para derrotar o chefe {boss['Nomes']} é: {best_weapon} o custo foi {(int)(custo)} caminho foi {best_weapon_path}")
else:
    print("Nenhuma arma adequada encontrada.")