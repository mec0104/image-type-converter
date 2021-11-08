# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:15:45 2021

@author: Mary
"""
from PIL import Image
import os

directory = (r'path\to\im\dir')

for filename in os.listdir(directory):
    if filename.endswith(".im_type"): #original image type
          path = os.path.join(directory,filename)
          im1 = Image.open(path)
          im1.save(filename,'im_type') #new image type
          
    if filename.endswith(".im_type"): #original image type
          path = os.path.join(directory,filename)
          im2 = Image.open(path)
          im2.save(filename,'im_type') #new image type 
    
  
