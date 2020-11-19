# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:06:05 2020

@author: JIt Shil
"""

import numpy as np
import cv2



def  click_event(event, x,y, flags, param):
    if event== cv2.EVENT_LBUTTONDOWN:
        print(x,' ',y)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x)+'  '+str(y)
        cv2.putText(img, text, (x,y), font, 0.5, (255,255,0),2)
        cv2.imshow('image', img)
        
        
img = cv2.imread('image4.jpeg', 0)
#img = np.zeros((512,512,3), np.uint8)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()        