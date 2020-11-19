# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:24:50 2020

@author: JIt Shil
"""


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('master.jpg',0)
lp = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1)
canny = cv.Canny(img, 100, 200)

lp = np.uint8(np.absolute(lp))
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
combined= cv.bitwise_or(sobelx, sobely)



titles =['original','laplacian','sobelx', 'sobely','canny','combined']
images = [img, lp, sobelx, sobely,canny,combined] 


for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

