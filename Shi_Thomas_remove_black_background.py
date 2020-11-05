'''
===============================================================================
-- Author:      Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 05/11/2020
-- Description:	This code is for removing black background of an image. 
-- Status:      In progress
================================================================================
'''

import cv2
import sys
import os
import math
import numpy as np


image = cv2.imread(sys.argv[1])

ho, wo = image.shape[:2]

image = cv2.resize(image, (int(wo*0.10), int(ho*0.10)))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

thresh = cv2.threshold(gray, 0, 255,
                       cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

img = image
blur = cv2.bilateralFilter(gray, 16, 50, 50)

corners = cv2.goodFeaturesToTrack(blur, 40, 0.1, 10)
corners = np.int0(corners)
xha = []
yha = []

for i in corners:
    x, y = i.ravel()

    xha.append(x)
    yha.append(y)

x0 = min(xha)
y0 = min(yha)
x1 = max(xha)
y1 = max(yha)
print(x0, x1, y0, y1)
cropped = img[y0:y1, x0:x1]

cv2.imwrite('cropped.jpg', cropped)
