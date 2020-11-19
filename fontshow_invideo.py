# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:05:20 2020

@author: JIt Shil
"""


import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 700)
cap.set(4, 700)


while(cap.isOpened()):
    ret, frame= cap.read()
    
    if ret == True:
       
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width'+ str(cap.get(3)) + 'Height' + str(cap.get(4))
        frame = cv2.putText(frame, text, (10,50), font, 1,(0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
     
    
cap.release()
cv2.destroyAllWindows()    
