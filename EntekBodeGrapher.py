# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:33:46 2024

@author: isaac
"""

import pandas as pd
import numpy as np  # Numpy is a useful module for scientific computing (similar language to MATLAB)
import matplotlib.pyplot as plt  # import the module for plotting data
import math  # import the module containing mathematical functions
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)     # Configure tick location and format

def Bode_grapher(const #Normalizing constant to turn current input into current density output if desired
               ,filenames,title,xlimits,ylimits,txt): #txt is true if dealing with a txt file, and false if dealing with a csv
    
    fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 
    ax.set_xlabel('log(frequency (Hz))')   # set the label of the x-axis
    #ax.set_ylabel('Z (Ohm)') # set the label of the y-axis
    
    #same general layout as NyquistGrapher
    
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
    Z1 = []
    Z2 = []
    Z3 = []
    Z4 = []
    Z5 = []
    Z6 = []
    Z7 = []
    colorlist=['g','b','r','y','k','c','m']
    datalistX=[X1,X2,X3,X4,X5,X6,X7]
    datalistY1=[Y1,Y2,Y3,Y4,Y5,Y6,Y7]
    datalistY2=[Z1,Z2,Z3,Z4,Z5,Z6,Z7]
    i=0
    while(i < len(filenames)):
        if txt == False:
            datalistX[i],datalistY1[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Lab/Project 5/Data Files/" + filenames[i] + ".csv", delimiter = ',', skiprows=1, unpack=True,
                   usecols=(0,1,2))
                     # Read data from a file scan1.csv and skip the first row.
        elif txt == True:
            datalistX[i],datalistY1[i],datalistY2[i]=np.loadtxt(fname="C:/Users/isaac/OneDrive/Documents/Electrochemistry Program/Echem Project/Data/txt files/Week 3/" + filenames[i] + ".txt", skiprows=1, unpack=True,
                   usecols=(0,3,4))
        ax.plot(np.log10(datalistX[i]),datalistY1[i]/const, '.', color='green')
        ax.set_ylabel('|Z| (Ohms)', color = 'green')
        ax2 = ax.twinx()
        ax2.plot(np.log10(datalistX[i]),datalistY2[i], '.', color=colorlist[i+1])
        ax2.set_ylabel('Phase angle (deg)',color = 'blue')
        i = i + 1
        
    #fig = plt.figure(figsize=(8, 6))    # Create a graph 'fig' which has 4 inches in width and 6 inches in height.
    #ax = fig.add_subplot(111)           # Create a subplot 'ax' in the figure 'fig'. 
    # subplot(abc): divide 'fig' into a (row)* b (column) sub-plots, 'ax' will be at the c-th sub-panel.
    #ax.plot(data_X, data_Y/0.0314159265358, '.', color='r')  
    # make a plot 'ax', with markers and lines, color=red
    if xlimits != None:
        ax.set_xlim(xlimits[0],xlimits[1])   # set the range of the x-axis of plot 'ax'
    if ylimits != None:
        ax.set_ylim(ylimits[0],ylimits[1])   # set the range of the y-axis
    #ax.set_xlabel('Potential, V')   # set the label of the x-axis
    #ax.set_ylabel('Current, mA/cm^2') # set the label of the y-axis
    #ax.legend(loc='upper left')       # place the legend at the 'upper left'
    ax.xaxis.set_minor_locator(MultipleLocator(10))   # add minor ticks for the x-axis
    ax.yaxis.set_minor_locator(AutoMinorLocator())    # add minor ticks for the y-axis
    ax.xaxis.grid(True, which='both') # add grids to the x-axis for both major and minor ticks
    ax.set_title(title)

    plt.show()   # display 'ax'