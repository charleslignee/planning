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
# Création du diagramme temps de travail quotidien
allData = pd.read_csv(adr + fileName, index_col = ['date'])
allData = allData.sort_index()
allData.plot(kind='bar', stacked = True, figsize = (10,8), rot = 60)
plt.legend(loc = 'lower left', bbox_to_anchor = (0.8,1.0))
plt.xlabel("Date",fontsize = 12)
plt.ylabel("temps de travail (h)",fontsize = 12)
plt.show()

# %%
# Création du diagramme temps de travail hebdomadaire
allData = pd.read_csv(adr + fileName)
allData = allData.sort_values(['date'])
allData['date'] = pd.to_datetime(allData['date'],errors = 'coerce')
allData.astype('int64').dtypes
allData['week_num'] = allData['date'].dt.isocalendar().week

weekData = allData.groupby(['week_num'])[['code','biblio','redaction','autre']].sum()
weekData.plot(kind='bar', stacked = True, figsize = (10,8), rot = 0)
plt.legend(loc = 'lower left', bbox_to_anchor = (0.8,1.0))
plt.xlabel("Semaine",fontsize = 12)
plt.ylabel("temps de travail (h)",fontsize = 12)
plt.show()
# %%
