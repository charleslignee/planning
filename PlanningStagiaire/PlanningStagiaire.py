# -*- coding: utf-8 -*-
# Created on Tue Dec 8 11:08:00:2021
# @package ArticleReview.ArticleReview
# @brief Outils pour les statistiques sur les articles des journaux
# @author: lionel
# ---------------------
import os
from PlanningStagiaire.ReadInput import ReadInput


class PlanningStagiaire(ReadInput):

    def __init__(self):
        ReadInput.__init__(self)
        self._adrPlanningStagiaire = self.__AdresseDuModule()

    # Définit l'adresse où se trouve le module
    # @return adr adresse du module
    def __AdresseDuModule(self):
        ''' Recupére l'adresse "de ce fichier" et on descend 
        de deux crans '''
        adrFile = os.path.dirname(os.path.realpath(__file__))
        adr = adrFile[0:adrFile.rfind(os.sep)] 
        return adr
     
    