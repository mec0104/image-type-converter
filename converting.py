# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:15:45 2021

@author: Mary
"""
from PIL import Image

import os
directory = (r'C:\Users\Mary\Documents\Fall 2021\Artificial Intelligence\Final Project\baseline_data\Buildings')

for filename in os.listdir(directory):
    if filename.endswith(".jpeg"):
          path = os.path.join(directory,filename)
          #print(path)
          im1 = Image.open(path)
          im1.save(filename,'png')) 
          
    if filename.endswith(".jpg"):
          path = os.path.join(directory,filename)
          #print(path)
          im1 = Image.open(path)
          im1.save(filename,'png')
    