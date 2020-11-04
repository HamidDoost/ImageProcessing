
# This code obtains keypoints from an RGB image and extract descriptor based on keypoints.

import cv2
import sys
import os
import numpy as np


def KAZE(image):

    # Vector_size value to be defined
    vector_size = 8

    alg = cv2.KAZE_create()
    kps = alg.detect(image)

    kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
    kps, dsc = alg.compute(image, kps)

    # You can increase vector_size to increase the length of descriptor
    needed_size = (vector_size * 64)
    if dsc is not None:
        dsc = dsc.flatten()
        if dsc.size < needed_size:

            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    else:
        dsc = np.ones(512)

    return kps, dsc


imagepath = sys.argv[1]
image = cv2.imread(imagepath)

keypoint, descriptor = KAZE(image)
cv2.drawKeypoints(image, keypoint, image, color=(0, 255, 0))
cv2.imwrite("outputimage.jpg", image)
