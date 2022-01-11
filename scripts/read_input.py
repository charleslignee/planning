#%%
import os
dirPath = os.path.dirname(os.path.realpath('__file__'))
dirSrc = dirPath[0:dirPath.rfind(os.sep)]
import sys
sys.path.append(".."+os.sep + "..")
sys.path.insert(0, dirSrc)
sys.path.insert(0, dirPath)
import pandas as pd

# Chargement des classes et de l'entrée
from PlanningStagiaire.PlanningStagiaire import PlanningStagiaire
to = PlanningStagiaire()
fileName = 'input.txt'
adr = to._adrPlanningStagiaire + os.sep + "Data" + os.sep
adrStore = to._adrPlanningStagiaire + os.sep + "_store" + os.sep

# Récupération du fichier .txt
inputData = to.ImportInput(adr + fileName)
inputData.to_csv(adr + 'input.csv',index = False)

# %%
