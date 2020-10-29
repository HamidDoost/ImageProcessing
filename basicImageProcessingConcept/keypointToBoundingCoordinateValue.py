# Extract keypoints from KAZE function (0_keypointAndDescriptor.py). Can be converted to boundary box coordinate value.

import cv2
import sys
import os
import numpy as np
from keypointAndDescriptor import KAZE


def coord(kps):
    corners = cv2.KeyPoint_convert(kps)
    corners = np.int0(corners)
    xs = []
    ys = []

    for i in corners:
        x, y = i.ravel()

        xs.append(x)
        ys.append(y)

    x0 = min(xs)
    y0 = min(ys)
    x1 = max(xs)
    y1 = max(ys)

    return x0, x1, y0, y1


imagepath = sys.argv[1]
image = cv2.imread(imagepath)

keypoint, descriptor = KAZE(image)
x0, x1, y0, y1 = coord(keypoint)

image = image[y0:y1, x0:x1]
cv2.imwrite("outputImage.jpg", image)
