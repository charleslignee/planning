#%%
import os
dirPath = os.path.dirname(os.path.realpath('__file__'))
dirSrc = dirPath[0:dirPath.rfind(os.sep)]
import sys
sys.path.append(".."+os.sep + "..")
sys.path.insert(0, dirSrc)
sys.path.insert(0, dirPath)
import pandas as pd
import matplotlib as plt

# Chargement des classes et de l'entrée
from PlanningStagiaire.PlanningStagiaire import PlanningStagiaire
to = PlanningStagiaire()
fileName = 'fichier.csv'
adr = to._adrPlanningStagiaire + os.sep + "Data" + os.sep
adrStore = to._adrPlanningStagiaire + os.sep + "_store" + os.sep

allData = pd.read_csv(adr + fileName)
allData.sort_values(by='date')



# %%
