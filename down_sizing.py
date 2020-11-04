
# This code  resize/rescale  many images for train


from imutils import paths
import numpy as np
import cv2
import os
import sys
from imutils.paths import list_images
import imutils
import time
import math

fileMode = "jpg"
print("[INFO] loading images...")
n = sys.argv[2]
nn = int(n)/10

imagePaths = sorted(list(paths.list_images(sys.argv[1])))
for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    filename = imagePath.split("\\")[-1]

    ho, wo = image.shape[:2]
    ar = wo/ho
    if ar < 1:
        W
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    ho, wo = image.shape[:2]
    orig = image
    resized = cv2.resize(image, (int(wo*nn), int(ho*nn)))
    cv2.imwrite(filename, resized)
