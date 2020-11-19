# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:18:25 2020

@author: JIt Shil
"""


import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 700)
cap.set(4, 700)


while(cap.isOpened()):
    ret, frame= cap.read()
    
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
     
    
cap.release()
cv2.destroyAllWindows()    