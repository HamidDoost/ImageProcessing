'''
===============================================================================
-- Author:      Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 05/11/2020
-- Description:	This code is for detection of corners keypoints by Shi-Thomas method. 
-- Status:      In progress
================================================================================
'''

import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(sys.argv[1])
ho, wo = image.shape[:2]
img = cv2.resize(image, (int(wo/10), int(ho/10)))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray_img, 20, 0.01, 100)

corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

cv2.imshow('corner', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
