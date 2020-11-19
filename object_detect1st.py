# -*- coding: utf-8 -*-
"""
Created on Tue May  5 08:43:57 2020

@author: JIt Shil
"""


import numpy as np
import cv2 as cv

def onChange(x):
    pass
cap = cv.VideoCapture(0)

cv.namedWindow('tracking')
cv.createTrackbar('LH', 'tracking', 0, 255, onChange)
cv.createTrackbar('LS', 'tracking', 0, 255, onChange)
cv.createTrackbar('LV', 'tracking', 0, 255, onChange)
cv.createTrackbar('UH', 'tracking', 0, 255, onChange)
cv.createTrackbar('US', 'tracking', 0, 255, onChange)
cv.createTrackbar('UV', 'tracking', 0, 255, onChange)

while 1:
    #frame = cv.imread('ball2.jpg')
    __, frame = cap.read()
    
    
    hsv= cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    lh = cv.getTrackbarPos('LH', 'tracking')
    ls= cv.getTrackbarPos('LS', 'tracking')
    lv= cv.getTrackbarPos('LV', 'tracking')
    uh= cv.getTrackbarPos('UH', 'tracking')
    us= cv.getTrackbarPos('US', 'tracking')
    uv= cv.getTrackbarPos('UV', 'tracking')
    
    
    lb = np.array([lh,ls,lv])
    ub = np.array([uh,us,uv])
    
    mask = cv.inRange(hsv, lb, ub)
    res = cv.bitwise_and(frame, frame, mask= mask)
    
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
 
    key = cv.waitKey(1)
    if key == 27:
        break
    
cap.release()    
cv.destroyAllWindows()    