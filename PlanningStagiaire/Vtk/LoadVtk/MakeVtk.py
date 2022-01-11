# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 13:54:47 2019

@author: ltrovale
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class MakeVtk():

    def __init__(self):
        self.dx = 1
    
    ## Défini, p, t et e pour le maillage en vtk 
    # @param data données en format pandas
    def MeshPte(self,data):
        dx = 1
        dy = 1
        Nx = max(set(data['i']))
        Ny = max(set(data['j']))
        t = {}
        p = {}
        e = {}
        ele = 0
        for k in data.index:  
            ''' Construction des sommets et assemblage '''
            A = data['i'].loc[k]+(data['j'].loc[k]-1)*(Nx+1) -1
            D = data['i'].loc[k]+1+(data['j'].loc[k]-1)*(Nx+1) -1
            B = data['i'].loc[k]+(data['j'].loc[k])*(Nx+1) -1
            C = data['i'].loc[k]+1+(data['j'].loc[k])*(Nx+1) -1
            t.update({k:[A,D,C,B]})
            ''' Calcul des coordonnées et assemblage'''
    #        pA = (data['i'].loc[k]*dx-dx/2,data['j'].loc[k]*dy-dy/2,0.0)
    #        pD = (data['i'].loc[k]*dx+dx/2,data['j'].loc[k]*dy-dy/2,0.0)
    #        pB = (data['i'].loc[k]*dx-dx/2,data['j'].loc[k]*dy+dy/2,0.0)
    #        pC = (data['i'].loc[k]*dx+dx/2,data['j'].loc[k]*dy+dy/2,0.0)
            
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
    
    def CreateVtk(self,file,p,t,data):
        src = open(file,"w",encoding='utf-8')
        src.write("# vtk DataFile Version 2.0 \n")
        src.write("\n")          
        src.write("ASCII\n")
        src.write("DATASET UNSTRUCTURED_GRID\n")
        src.write("POINTS " + str(len(p)) +" float \n")
        for node in sorted(p.keys()):
            src.write(str(p[node][0]) +"    "+str(p[node][1]) +"    "+str(p[node][2]) +"\n")
        src.write("CELLS   " + str(len(t)) +"   " + str(len(t)*5)+" \n")
        for sommet in t.values():
            src.write(str(4)+"   " + str(sommet[0]) +"   "+
                      str(sommet[1]) +"   "+
                      str(sommet[2]) +"   "+
                      str(sommet[3]) +"\n")
        src.write("CELL_TYPES " + str(len(t)) +" \n")
        for sommet in t.values():
            src.write(str(9) +"\n")
        #src.write("POINT_DATA  "+ str(len(p)) + "\n")
        src.write("CELL_DATA  "+ str(len(data.index)) + "\n")
        src.write("SCALARS Temperature float\n")
        src.write("LOOKUP_TABLE default\n")
        for coord in data.index:
            src.write(str(12.0) +"\n")
            
    ## Trace le maillage        
    def Graphique(self,t,p,data):
        ''' Trace les points et dessine les rectangles'''
        pp = np.array([])
        for i in sorted(p.keys()):
            pp = np.append(pp,np.array(p[i]))
        P = np.reshape(pp,(len(p),3))
        
        plt.scatter(P[:,0], P[:,1])
        for k in data.index: 
            self.__traceQuadra(t,k,P)
        plt.show() 
        
    ## Trace un element    
    def __traceQuadra(self,t,k,P):
        x = []
        y = []
        for node in t[k]:
            x.append(P[node,0])
            y.append(P[node,1])
        x.append(P[t[k][0],0])
        y.append(P[t[k][0],1])
        plt.plot(x,y)
        
        