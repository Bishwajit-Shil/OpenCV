# -*- coding: utf-8 -*-
"""
Created on Tue May  5 08:02:20 2020

@author: JIt Shil
"""


import numpy as np 
import cv2 as cv

def onChange(x):
    print(x)
    
switch= '0 : OFF \n 1: ON'    

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, onChange)
cv.createTrackbar('G', 'image', 0, 255, onChange)
cv.createTrackbar('R', 'image', 0, 255, onChange)
cv.createTrackbar(switch, 'image', 0, 1, onChange)



while True:
    cv.imshow('image', img)
    k = cv.waitKey(1)  & 0xFF 
    if k == 27:
        break
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')
    
    if s == 1:
        img[:] = [b,g,r]
    else:
        img[:] = 0
        
    
    
    
cv.destroyAllWindows()    