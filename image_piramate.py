# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:37:39 2020

@author: JIt Shil
"""


import cv2
import matplotlib.pyplot as plt

img = cv2.imread('ronaldo.jpg')
layar = img.copy()
gp = [layar]

for i in range(6):
    layar = cv2.pyrDown(layar)
    gp.append(layar)
    cv2.imshow(str(i), layar)
   
#cv2.imshow('original photo', img)    
    
    
    
layar = gp[5]
lp = [layar] 

for i in range(5, 0, -1):
    gaussian_extend = cv2.pyrUp(gp[i])
    laplacian  = cv2.subtract(gp[i-1], gaussian_extend)
    cv2.imshow(str(i), laplacian)
    
cv2.waitKey(0)
cv2.destroyAllWindows()

