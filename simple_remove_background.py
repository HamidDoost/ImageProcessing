'''
===============================================================================
-- Author:		Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 05/11/2020
-- Description:	This code is for removing background and cropping of an image. 
-- Status:      In progress
================================================================================
'''


# Simple remove background and cropping

import cv2
import sys
import os
import numpy as np

imagepath = sys.argv[1]
image = cv2.imread(imagepath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

thresh = cv2.threshold(gray, 127, 255,
                       cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

pixelpoints = np.transpose(np.nonzero(thresh))
nom = len(pixelpoints)
xs = []
ys = []
for i in range(0, nom-1):
    xs.append(pixelpoints[i][1])
    ys.append(pixelpoints[i][0])
x0 = min(xs)
y0 = min(ys)
x1 = max(xs)
y1 = max(ys)
image = image[y0:y1]
print(x0, x1, y0, y1)
