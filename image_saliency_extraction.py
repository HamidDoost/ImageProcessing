'''
============================================================
-- Author:		Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 05/11/2020
-- Description:	This code is for extracting image saliancy.
-- Status:      In progress
=============================================================

'''
import cv2
import sys
import os
import numpy as np

saliency = cv2.saliency.StaticSaliencyFineGrained_create()
image = cv2.imread(sys.argv[1])
image0 = cv2.imread(sys.argv[1], 0)

(success, saliencyMap) = saliency.computeSaliency(image)
saliencyMap = (saliencyMap * 255).astype("uint8")
mask = cv2.threshold(saliencyMap, 100, 255,
                     cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# kernal size depends on image size
kernel = np.ones((17, 17), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

mask = mask == 0
coords = np.argwhere(mask)
x0, y0 = coords.min(axis=0)
x1, y1 = coords.max(axis=0) + 1
image = image[x0:x1, y0:y1]
print(x0, x1, y0, y1)
