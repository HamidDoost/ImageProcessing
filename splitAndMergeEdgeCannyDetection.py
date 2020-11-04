'''
====================================================================================
-- Author:		Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 28/10/2020
-- Description:	This code is for splitting and merging edge by Canny Detection.
                Edges from this code can be used for Laplacian and Sobel Combined.
====================================================================================
'''

import cv2
import sys
import os
import numpy as np


def edges(image):
    blue, green, red = cv2.split(image)
    blue_edges = cv2.Canny(blue, 200, 250)
    green_edges = cv2.Canny(green, 200, 250)
    red_edges = cv2.Canny(red, 200, 250)
    edges0 = blue_edges | green_edges | red_edges
    edges1 = cv2.Canny(image, 200, 400)
    return edges0


image = cv2.imread(sys.argv[1])
edges0 = edges(image)
