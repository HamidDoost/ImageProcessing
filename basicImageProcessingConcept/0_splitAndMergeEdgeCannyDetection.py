'''
canny
'''

import cv2
import sys
import os
import numpy as np

image = cv2.imread(sys.argv[1])

blue, green, red = cv2.split(image)
blue_edges = cv2.Canny(blue, 200, 250)
green_edges = cv2.Canny(green, 200, 250)
red_edges = cv2.Canny(red, 200, 250)
edges0 = blue_edges | green_edges | red_edges
edges1 = cv2.Canny(image, 200, 400)
