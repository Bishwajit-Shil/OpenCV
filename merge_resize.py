# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:56:02 2020

@author: JIt Shil
"""


import cv2 

img= cv2.imread('image4.jpeg')
img2= cv2.imread('image7.jpg')

print(img.shape)
print(img.size)
print(img.dtype)
#print(img)

b,g,r = cv2.split(img)
img= cv2.merge((b,g,r))

fuck = img[736:824,921:988 ]
img[667:692, 907:952]= fuck
#img= cv2.resize(img,(512,512))
#img2= cv2.resize(img2,(512,512))

#dst= cv2.addWeighted(img,0.3, img2,0.7,0)
#cv2.imshow('imagesize', dst)

cv2.imshow('resize', img)
cv2.waitKey(0)
cv2.destroyAllWindows()