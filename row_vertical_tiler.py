'''
===============================================================================
-- Author:      Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 05/11/2020
-- Description:	This code is for vertical tiling of images. 
-- Status:      In progress
================================================================================
'''


from imutils import paths
import numpy as np
import cv2
import os
import sys
from imutils.paths import list_images

fileMode = "jpg"
print("[INFO] loading images...")
n = sys.argv[2]
nn = int(n)
imagePaths = sorted(list(paths.list_images(sys.argv[1])))
for imagePath in imagePaths:
    image = cv2.imread(imagePath)

    filename = imagePath.split("\\")[2]
    print(filename)

    ho, wo = image.shape[:2]
    ar = wo/ho
    if ar > 1:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    ho, wo = image.shape[:2]
    partition = int(ho/nn)
    orig = image
    for ii in range(nn-1):
        part = image[0:partition, :]
        image = image[partition:ho, :]
        ho, wo = image.shape[:2]
        cv2.imwrite(str(ii)+"_"+filename, part)
