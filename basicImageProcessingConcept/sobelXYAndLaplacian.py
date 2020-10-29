'''
laplacian and sobelCombined
'''
import cv2
import sys
import os
import numpy as np
from splitAndMergeEdgeCannyDetection import edges


def sobelCombined(image):
    edges0 = edges(image)
    # edges0 can be used from Canny
    lap = cv2.Laplacian(edges0, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))

    # edges0 can be used from Canny
    sobelX = cv2.Sobel(edges0, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(edges0, cv2.CV_64F, 0, 1)

    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))

    sb = cv2.bitwise_or(sobelX, sobelY)
    return sb


imagepath = sys.argv[1]
image = cv2.imread(imagepath)

sb = sobelCombined(image)
