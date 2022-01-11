# -*- coding: utf-8 -*-
#  Created on Mon Jan  10 9:00:00 2022
## @package connectBdd.ConnexionDataBasePsql
#  @brief Lecture et traitement 
#  @author: clignee
# ---------------------- 


import os
from re import T
import sys
import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.series import Series
import copy

class ReadInput():
    ''' Outils de connexion vers la base de données utilisant
        le fichier de connexion se trouvant dans le même répertoire.
            - Cette classe comporte un test de connexion lors de son 
              execution entant que programme principal.
    
        Attributs
        ---------
            paramBdd [dict] : paramètres de la base de données
            engine [sqlalchemy] : point de connexion vers la base
    '''           
    
    
    ## Initialisation de la classe et lancement de deux méthodes
    def __init__(self, connexionFile = "BddParamIn.txt"):

        ''' Initialisation de la classe et déclaration des attributs.
            La lecture du fichier de connexion est effectué au cours
            de l'initialisation ainsi qu l'établissement du point de
            connexion vers la base est crée.

        Arguments optionnel
        -------------------
            connexionFile [str] : nom du fichier des paramètres de connexion 
        '''        
        self.fileName = 'init'
        

    def ImportInput(self,file_name):
        ''' Lit le fichier contenant les tâches et leurs durées.
            Le fichier comporte différents identificateurs détaillés dans le
            fichier 'README.md'. Ces identificateurs permettent de récupérer
            les tâches et leurs durées sur les différents jours ou semaines. 
            Le fichier est lu ligne par ligne et les données nécessaires au
            traitement sont stockées dans une variable.
        '''
        print("Lecture du fichier")
        inputData = pd.DataFrame()
        self.fileName = file_name
        with open(file_name, "r", encoding="utf-8") as input_file:
            for lign in input_file:                    
                if lign[:4] == "Date":
                    ticket = {}
                    dailyData = lign.split(' ')
                    for data in dailyData:                                                
                        ticket.update({data.split(':')[0].strip():data.split(':')[1].strip()})
                    inputData = pd.concat([inputData,pd.DataFrame(pd.Series(ticket)).T])
        
        return inputData

                       
    
   



# Programme de test de la classe
if __name__=='__main__':
    fileName = 'input_test.txt'
    to = ReadInput()
    to._ReadParam(fileName)