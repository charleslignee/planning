# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 07:36:46 2019

@author: ltrovale
"""
import os
import pandas as pd

""" Define the directory for files """ 
dirPath = os.path.dirname(os.path.realpath(__file__))
dirSrc = dirPath[0:dirPath.rfind(os.sep)]
filename = dirPath + "\\_Store\\Paul\\Coord.txt"

data = pd.read_csv(filename,sep='\t')


def VtkMesh(data):
    Nx = max(set(data['i']))
    Ny = max(set(data['j']))
    t = {}
    p = {}
    e = {}
    ele = 0
    for k in data.index:  
        ''' Construction des sommets et assemblage '''
        A = data['i'].loc[k]+(data['j'].loc[k]-1)*(Nx+1)
        D = data['i'].loc[k]+1+(data['j'].loc[k]-1)*(Nx+1)
        B = data['i'].loc[k]+(data['j'].loc[k])*(Nx+1)
        C = data['i'].loc[k]+1+(data['j'].loc[k])*(Nx+1)
        t.update({k:[A,D,B,C]})
        ''' Calcul des coordonnées et assemblage'''
        pA = (data['rint'].loc[k],data['z_bas'].loc[k],0.0)
        pD = (data['rext'].loc[k],data['z_bas'].loc[k],0.0)
        pB = (data['rint'].loc[k],data['z_haut'].loc[k],0.0)
        pC = (data['rext'].loc[k],data['z_haut'].loc[k],0.0)
        if not A in p.keys():
            p.update({A:pA})
        if not D in p.keys():
            p.update({D:pD})
        if not B in p.keys():
            p.update({B:pB})
        if not C in p.keys():
            p.update({C:pC})
        ''' Construction des bords '''
        if data['j'].loc[k]==1:
            ele += 1
            e.update({ele:[A,D,1]})
        elif data['j'].loc[k]==Ny:
            ele += 1
            e.update({ele:[B,C,3]})
        if data['i'].loc[k]==1:
            ele += 1
            e.update({ele:[A,B,4]})
        elif data['i'].loc[k]==Nx:
            ele += 1
            e.update({ele:[B,C,2]})
    return p,t,e

p,t,e = VtkMesh(data)


src = open('test.vtk',"w")
src.write("# vtk DataFile Version 2.0 \n")
src.write(" \n")          
src.write("ASCII\n")
src.write("DATASET UNSTRUCTURED_GRID\n")
src.write("POINTS " + str(len(p)) +" float \n")
for coord in p.values():
    src.write(str(coord[0]) +"    "+str(coord[1]) +"    "+str(coord[2]) +"   \n")
src.write("CELLS   " + str(len(t)) +"   " + str(len(t)*5)+" \n")
for sommet in t.values():
    src.write(str(4)+"   " + str(sommet[0]-1) +"  "+
              str(sommet[1]-1) +"   "+
              str(sommet[2]-1) +"   "+
              str(sommet[3]-1) +"    \n")
src.write("CELLS_TYPES " + str(len(t)) +" \n")
for sommet in t.values():
    src.write(str(8) +"  \n")
#src.write("POINT_DATA  "+ str(len(p)) + "\n")
#src.write("SCALARS Temperature float \n")
#src.write("LOOKUP_TABLE default\n")
#for coord in p.values():
#    src.write(str(12) +"  \n")





        
        

        



