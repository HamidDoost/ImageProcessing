'''
======================================================================
-- Author:      Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 29/10/2020
-- Description:	This code is for extracting of corners from an image.
=======================================================================

'''
import cv2
import sys
import os
import numpy as np
from sobelXYAndLaplacian import sobelCombined


# sobelCombined can be used from SobelXYAndLaplacian or from SaliencyThresshold or ordinary treshold
def corners(image):
    sb = sobelCombined(image)
    corners = cv2.goodFeaturesToTrack(sb, 25, 0.01, 10)
    corners = np.int0(corners)
    xs = []
    ys = []
    for i in corners:
        x, y = i.ravel()
        cv2.circle(image, (x, y), 3, 255, -1)

        xs.append(x)
        ys.append(y)

    x0 = min(xs)
    y0 = min(ys)
    x1 = max(xs)
    y1 = max(ys)
    print(x0, x1, y0, y1)
    return x0, x1, y0, y1


imagepath = sys.argv[1]
image = cv2.imread(imagepath)
x0, x1, y0, y1 = corners(image)
image = image[y0:y1]
cv2.imwrite("outputimage.jpg", image)
