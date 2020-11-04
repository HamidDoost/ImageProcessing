'''
===============================================================================
-- Author:		Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 05/11/2020
-- Description:	This code is for removing black margin of an image. 
                It can be used for cropping margins of an image.
-- Status:      In progress
================================================================================
'''

import numpy as np
import glob
import cv2
import os
import sys


def auto_canny(image):
    sigma = 0.33
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    return edged


for root, dirs, files in os.walk(sys.argv[1]):
    for filename in files:
        ext = filename[filename.rfind("."):].lower()
        fn = os.path.join(root, filename)
        image = cv2.imread(os.path.join(root, filename))
        h, w = image.shape[:2]
        image = cv2.resize(image, (int(w/10), int(h/10)))
        mask = auto_canny(image) == 255
        coords = np.argwhere(mask)

        x0, y0 = coords.min(axis=0)
        x1, y1 = coords.max(axis=0) + 1

        cropped = image[x0:x1, y0:y1]

        cv2.imwrite(filename, cropped)
