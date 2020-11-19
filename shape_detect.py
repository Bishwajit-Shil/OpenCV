# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:45:33 2020

@author: JIt Shil
"""


import cv2

img = cv2.imread('shape.png')
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
__, thrash = cv2.threshold(imggray, 240,200, cv2.THRESH_BINARY)
contours, __ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0,0,0))
    x= approx.ravel()[0]
    y= approx.ravel()[1]
    #print(x, y)
    lenght = len(approx)
    if lenght == 3:
        cv2.putText(img, 'triangle', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0,0,255))
    elif lenght == 4:
        cv2.putText(img, 'rectangular', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0,0,255))
    elif lenght == 12:
        x1, y1, w, h = cv2.boundingRect(approx)
        
        if (float(w)/float(h))>= 1:
            cv2.putText(img, 'Love', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0,0,255))
        else:
            cv2.putText(img, 'star', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0,0,255))
    else:
        cv2.putText(img, 'circle', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0,0,255))
        
        
cv2.imshow('shape.jpg', img)
cv2.imwrite('shaperesult.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
