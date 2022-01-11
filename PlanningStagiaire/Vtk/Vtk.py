# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 07:36:46 2019

@author: ltrovale
"""
import os
import pandas as pd
from LoadVtk.MakeVtk import MakeVtk

""" Define the directory for files """ 
dirPath = os.path.dirname(os.path.realpath(__file__))
dirSrc = dirPath[0:dirPath.rfind(os.sep)]
filename = dirPath + "\\_Store\\Paul\\Coord.txt"
data = pd.read_csv(filename,sep='\t')
file = 'test.vtk'
to = MakeVtk()

p,t,e = to.MeshPte(data)
to.Graphique(t,p,data)
to.CreateVtk(file,p,t,data)








        

       



