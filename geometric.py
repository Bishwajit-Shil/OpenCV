# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:00:57 2020

@author: JIt Shil
"""


import cv2

img= cv2.imread('image4.jpeg' , 0)

img= cv2.line(img, (0,0), (255,255), (0,0,255),  5) 

cv2. imshow('image' , img)

cv2.waitKey(0)
cv2.destroyAllWindows()