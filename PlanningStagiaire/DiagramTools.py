import pandas as pd
import matplotlib.pyplot as plt

class DiagramTools():

    def __init__(self):
        pass

    def ShowHisto(self, adr, filename,freq):
        ''' Récupère le fichier et trace l'histogramme.
            adr = adresse du fichier.
            filename = nom du fichier.
            freq = fréquence des données : quotidiennes (freq = "D")
            ou hebdomadaires (freq = "W").
        '''
        if freq == "D":
            # Construction du diagramme quotidien
            self.allData = pd.read_csv(adr + filename, index_col = ['date'])
            self.allData = self.allData.sort_index()
            self.allData.plot(kind='bar', stacked = True, figsize = (10,8), rot = 60)
            plt.legend(loc = 'lower left', bbox_to_anchor = (0.8,1.0))
            plt.xlabel("Date",fontsize = 12)
            plt.ylabel("temps de travail (h)",fontsize = 12)
            plt.show()
        elif freq == "W":
            # Construction du diagramme hebdomadaire
            self.allData = pd.read_csv(adr + filename)
            self.allData = self.allData.sort_values(['date'])
            self.allData['date'] = pd.to_datetime(self.allData['date'],errors = 'coerce')
            self.allData.astype('int64').dtypes
            self.allData['week_num'] = self.allData['date'].dt.isocalendar().week

            self.weekData = self.allData.groupby(['week_num'])[['code','biblio','redaction','autre']].sum()
            self.weekData.plot(kind='bar', stacked = True, figsize = (10,8), rot = 0)
            plt.legend(loc = 'lower left', bbox_to_anchor = (0.8,1.0))
            plt.xlabel("Semaine",fontsize = 12)
            plt.ylabel("temps de travail (h)",fontsize = 12)
            plt.show()