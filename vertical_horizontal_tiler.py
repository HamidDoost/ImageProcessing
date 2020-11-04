'''
===============================================================================
-- Author:		Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 05/11/2020
-- Description:	This code is for horizental or vertical tiling of images.
                Parameters are Folder name and Number of tiles.
                It works better on original scale images.
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

    filename = imagePath.split("\\")[-1]
    print(filename)

    ho, wo = image.shape[:2]
    ar = wo/ho
    if ar < 1:

        partition = int(ho/nn)
        orig = image
        for ii in range(nn):

            part = image[0:partition, :]
            image = image[partition:ho, :]
            ho, wo = image.shape[:2]
            cv2.imwrite(str(ii)+"_"+filename, part)

    else:
        partition = int(wo/nn)
        orig = image
        for ii in range(nn):

            part = image[:, 0:partition]
            image = image[:, partition:wo]
            ho, wo = image.shape[:2]
            cv2.imwrite(str(ii)+"_"+filename, part)
