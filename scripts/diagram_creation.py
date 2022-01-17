#%%
from cProfile import label
import os
dirPath = os.path.dirname(os.path.realpath('__file__'))
dirSrc = dirPath[0:dirPath.rfind(os.sep)]
import sys
sys.path.append(".."+os.sep + "..")
sys.path.insert(0, dirSrc)
sys.path.insert(0, dirPath)
import pandas as pd
import matplotlib.pyplot as plt
from PlanningStagiaire.PlanningStagiaire import PlanningStagiaire

#%%
# Récupération des classes et des données d'entrée
to = PlanningStagiaire()
fileName = 'fichier.csv'
adr = to._adrPlanningStagiaire + os.sep + "Data" + os.sep
adrStore = to._adrPlanningStagiaire + os.sep + "_store" + os.sep
#%%
# Création des diagrammes de temps de travail
to.ShowHisto(adr,fileName,'D')
to.ShowHisto(adr,fileName,'W')
# %%
