# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:01:01 2020

@author: JIt Shil
"""


# -*- coding: utf-8 -*-
"""
Created on Tue May  5 10:09:03 2020

@author: JIt Shil
"""


import cv2 as cv

import matplotlib.pyplot as plt

img = cv.imread('ball1.jpg',1)
cv.imshow('image', img)


plt.imshow(img)
plt.show()






cv.waitKey(0) 
cv.destroyAllwindows()