import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import networkx as nx

def aleatorize(df):
    if len(df) >= 10:
        aleatorize = random.sample(range(len(df)), 10)
        new_df = df.iloc[aleatorize].copy()
    else:
        aleatorize = random.sample(range(len(df)), len(df))
        new_df = df.iloc[aleatorize].copy()
    return new_df

def dataFrame_creator(df_og):
    df = df_og.copy()

    df_magic = df[df['Magical damage'] > 0].copy()
    df_magic = aleatorize(df_magic)
    df_magic = df_magic.sort_values(by=['Magical damage'], ascending=False)  # Atualize o DataFrame com a classificação
    df_magic = df_magic.reset_index(drop=True)

    df_fire = df[df['Fire damage'] > 0].copy()
    df_fire = aleatorize(df_fire)
    df_fire = df_fire.sort_values(by=['Fire damage'], ascending=False)  # Atualize o DataFrame com a classificação
    df_fire = df_fire.head(10).reset_index(drop=True)

    df_lightning = df[df['Lightning damage'] > 0].copy()
    df_lightning = aleatorize(df_lightning)
    df_lightning = df_lightning.sort_values(by=['Lightning damage'], ascending=False)  # Atualize o DataFrame com a classificação
    df_lightning = df_lightning.head(10).reset_index(drop=True)

    df_physical = df[df['Physical damage'] > 0].copy()
    df_physical = aleatorize(df_physical)
    df_physical = df_physical.sort_values(by=['Physical damage'], ascending=False)  # Atualize o DataFrame com a classificação
    df_physical = df_physical.reset_index(drop=True)


    return df_physical, df_lightning, df_fire, df_magic


def imprimeGrafo(G):
    # Desenhe o grafo
    pos = nx.circular_layout(G)  # Layout para organizar os nós
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')

    # Exiba o grafo (opcional)
    plt.show()

    # Salve o grafo como imagem
    plt.savefig("grafo.png")
