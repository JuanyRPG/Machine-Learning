# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jjP1g_IMymuqjoTRHeI9nmBRZTq47Erz
"""

import pandas as pd

datos = pd.read_csv('pokedex_(Update_04.21).csv')

datos.head(11)



datos.tail(21)

datos.shape

datos.size

datos['name'].head()