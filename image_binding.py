# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:29:11 2020

@author: JIt Shil
"""


import cv2
import numpy as np


g_apple = cv2.imread('green.jpg')
r_apple = cv2.imread('red.jpg')
gr_apple = np.hstack((g_apple[:, :256], r_apple[:, 256:]))


g_apple = g_apple.copy()
gp_apple = [g_apple]
for i in range(6):
    g_apple = cv2.pyrDown(g_apple)
    gp_apple.append(g_apple)
    
r_apple = r_apple.copy()
gp_rapple= [r_apple]
for i in range(6):
    r_apple = cv2.pyrDown(r_apple)
    gp_rapple.append(r_apple)
    
    
    
g_apple = gp_apple[5]
lpg_apple = [g_apple]
for i in range(5,0, -1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_expanded)
    lpg_apple.append(laplacian)
    
    
r_apple = gp_rapple[5]
lpr_apple = [r_apple]
for i in range(5,0, -1):
    gaussian_expanded = cv2.pyrUp(gp_rapple[i])
    laplacian = cv2.subtract(gp_rapple[i-1], gaussian_expanded)
    lpr_apple.append(laplacian)    
    
    
apple_orange_pyramid = []
n=0
for gapple_lap, rapple_lap in zip(lpg_apple, lpr_apple):
    n += 1
    cols,rows,ch = gapple_lap.shape
    laplacian = np.hstack((gapple_lap[:, :int(cols/2)], rapple_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)
    
    
apple_orange_reconstruct = apple_orange_pyramid[0]

for i in range(1,6):
    apple_orange_reconstruct =cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)
    



print(g_apple.shape)
print(r_apple.shape)


cv2.imshow('green apple', g_apple)
cv2.imshow('Red apple', r_apple)
cv2.imshow('combained', gr_apple)
cv2.imshow('green and red apple combination', apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()

