# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:05:54 2020

@author: JIt Shil
"""


import  cv2
img = cv2.imread('image4.jpeg', 0)
#print(img)
cv2.imshow('image', img)
k= cv2.waitKey(0)


if k==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('result.png', img)
    cv2.destroyAllWindows()
