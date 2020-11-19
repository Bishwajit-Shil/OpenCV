# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:21:12 2020

@author: JIt Shil
"""


import cv2
import numpy as np


cap = cv2.VideoCapture('football.mp4')

ret, frame1 = cap.read()
ret, frame2 = cap.read()


while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff,  cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    __, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, __=cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        
        if  cv2.contourArea(contour) <800 or cv2.contourArea(contour) > 5000 :
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0),2)
    
    cv2.imshow('motion detecting', frame1)
    frame1= frame2
    ret, frame2 = cap.read()
    
    
    
    
    if cv2.waitKey(40) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()
