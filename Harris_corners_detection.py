'''
=====================================================================
-- Author:      Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 05/11/2020
-- Description:	This code is for corners detection by Harris method
-- Status:      In progress
=====================================================================

'''

import cv2
import os
import sys
import numpy as np


def cornerHarris(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)

    dst = cv2.dilate(dst, None)

    img[dst > 0.01*dst.max()] = [0, 0, 255]

    cv2.imshow('dst', img)
    cv2.waitKey(0)


img = cv2.imread(sys.argv[1])
h, w = img.shape[:2]
img = cv2.resize(img, (int(w/10), int(h/10)))


cornerHarris(img)
cv2.imwrite('harris.png', img)
