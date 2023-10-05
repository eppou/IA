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
    pos = nx.spring_layout(G, seed=42, k=2.5, iterations=500) 
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=9, font_weight="bold")
    
    nx.draw_networkx_edges(G, pos, edge_color="red", width=2)

    plt.title("Grafo com arestas ligadas a A (Layout spring ajustado)")
    plt.axis("off")  

    # Exiba o gráfico
    plt.savefig("grafo.png")
