# Reduce thecolor rage to three channels of RGB with maximum filter

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
