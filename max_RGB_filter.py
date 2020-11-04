'''
===============================================================================
-- Author:		Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 29/10/2020
-- Description:	This code is for reducing the colour range to three channels 
                of RGB with maximum filter.
                It can be used for filtering colours.
-- Status:      In progress
================================================================================
'''


import cv2
import sys
import os
import numpy as np

imagepath = sys.argv[1]
image = cv2.imread(imagepath)
(B, G, R) = cv2.split(image)

M = np.maximum(np.maximum(R, G), B)
R[R < M] = 0
G[G < M] = 0
B[B < M] = 0

filter = cv2.merge([B, G, R])
