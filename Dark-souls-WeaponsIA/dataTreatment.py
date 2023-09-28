import numpy as np
import pandas as pd
import random

def dataFrame_creator(df_og):
    df = df_og.copy()
    df.sort_values(by=['Magical damage'], inplace=True)
    df_magic = df.head(10).copy()
    df.sort_values(by=['Fire damage'], inplace=True)
    df_fire = df.head(10).copy()
    df.sort_values(by=['Lightning damage'], inplace=True)
    df_lightning = df.head(10).copy()
    df.sort_values(by=['Physical damage'], inplace=True)
    df_physical = df.head(10).copy()

    return df_physical, df_lightning, df_fire, df_magic
