# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 03:29:15 2024

@author: isaac
"""
import pandas as pd
import numpy as np  # Numpy is a useful module for scientific computing (similar language to MATLAB)
import matplotlib.pyplot as plt  # import the module for plotting data
import math  # import the module containing mathematical functions
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)     # Configure tick location and format

#same general layout as Nyquist grapher. Make sure to replace my file path with your own.
#Includes fitting function.


def Cottrell_fit(const #Normalizing constant to turn current input into current density output if desired
               ,filenames,title,xlimits,yunits,ylimits,txt):
    
    fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 
    ax.set_xlabel('time^(-1/2)')   # set the label of the x-axis
    ax.set_ylabel('Current ' + yunits) # set the label of the y-axis
    
    X1 = []
    X2 = []
    X3 = []
    X4 = []
    X5 = []
    X6 = []
    X7 = []
    Y1 = []
    Y2 = []
    Y3 = []
    Y4 = []
    Y5 = []
    Y6 = []
    Y7 = []
    colorlist=['g','b','r','y','k','c','m']
    datalistX=[X1,X2,X3,X4,X5,X6,X7]
    datalistY=[Y1,Y2,Y3,Y4,Y5,Y6,Y7]
    xp = np.linspace(-10,10,10000)  #index for graphing fit
    i=0
    while(i < len(filenames)):
        if txt == False:
            datalistX[i],datalistY[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Lab/Project 4/Data Files/" + filenames[i] + ".csv", delimiter = ',', skiprows=1, unpack=True,
                   usecols=(2,5))
                     # Read data from a file scan1.csv and skip the first row.
        elif txt == True:
            datalistX[i],datalistY[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Echem Project/Data/txt files/Week 5/" + filenames[i] + ".txt", skiprows=1, unpack=True,
                   usecols=(0,1))
        i = i + 1
        
        #fitting is also within loop for easy multi-fit functionality
        newX = 1/(datalistX[0]**0.5)
        newY = datalistY[0]/const
        
        ax.plot(newX, newY, '.', color='g',label=filenames[0])
    
        z = np.polyfit(newX,newY,1) #obtain linear fit
    
        zp = xp*z[0] + z[1] #y-axis data for fit that will be graphed
    
        ax.plot(xp,zp,'--',color = 'b',label = 'fit')   #plot
            
    

    if xlimits != None:
        ax.set_xlim(xlimits[0],xlimits[1])   # set the range of the x-axis of plot 'ax'
    if ylimits != None:
        ax.set_ylim(ylimits[0],ylimits[1])   # set the range of the y-axis

    ax.legend(loc='lower left')       # supported values are 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
    ax.xaxis.set_minor_locator(MultipleLocator(10))   # add minor ticks for the x-axis
    ax.yaxis.set_minor_locator(AutoMinorLocator())    # add minor ticks for the y-axis
    ax.xaxis.grid(True, which='both') # add grids to the x-axis for both major and minor ticks
    if title != None:
        ax.set_title(title)

    plt.show()   # display 'ax'
    return z[0]