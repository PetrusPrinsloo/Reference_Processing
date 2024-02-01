# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:33:49 2024

@author: pjcp0
"""

import pandas as pd

# import numpy as np

df1 = pd.read_excel("Reference_list.xlsx", skiprows = 1)

df2 = pd.read_excel("SciFinder_hits.xlsx")

Patent = df2[df2["Type"] == "Patent"]

Article = df2[df2["Type"] == "Article"]

df = pd.concat([df1, Article], ignore_index = True)

df ["DOI"] = df['doi'].fillna(" ") + df['DOI/Patent'].fillna(" ")

df.drop(['doi'],inplace=True,axis=1)
df.drop(['DOI/Patent'],inplace=True,axis=1)
df.drop(['Publication Year'],inplace=True,axis=1)
df.drop(['Category'],inplace=True,axis=1)
df.drop(['Type'],inplace=True,axis=1)
df.drop(['Retrieved'],inplace=True,axis=1)
df.drop(['Citation status'],inplace=True,axis=1)

df3 = df[df["DOI"] != "  "]

