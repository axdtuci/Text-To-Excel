# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 12:39:34 2023

@author: singha9
"""

import os
import easygui
import pandas as pd

fileList = easygui.fileopenbox(multiple=True)
#print(fileList)
for filename in fileList:
    directory = os.path.dirname(filename)#os.getcwd() # assign directory
    #print (directory) # Check the directory address
    for filename in os.listdir(directory): # iterate over files in that directory
        f = os.path.join(directory,  filename)   
        if filename.endswith('.txt'):
        #fName = os.path.basename(directory)  #Get the input folder name to use in the output filename Alternate #fName = os.path.splitext((os.path.basename(directory)))
        #print(fName) # or print(os.path.splitext(fName)[0])
            df = pd.read_csv(f) # can replace with df = pd.read_table('input.txt') for '\t'
            df.to_excel(filename+'.xlsx', filename, index=False)
        