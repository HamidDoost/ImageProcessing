

'''
Extract Super Pixels of images to obtain boundaries of SLIC segmnetation.
In fact, finds keypoints for SLIC segmentation.
'''

import cv2
import sys
import os
import numpy as np


def super(img):
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		gray = np.float32(gray)
		dst = cv2.cornerHarris(gray, 2, 3, 0.04)
		dst = cv2.dilate(dst, None)
		ret, dst = cv2.threshold(dst, 0.01*dst.max(), 255, 0)
		dst = np.uint8(dst)

		ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

		criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
		corners = cv2.cornerSubPix(gray, np.float32(
		    centroids), (15, 15), (-15, -15), criteria)

		res = np.hstack((centroids, corners))
		res = np.int0(res)
		img[res[:, 1], res[:, 0]] = [0, 0, 255]
		img[res[:, 3], res[:, 2]] = [0, 255, 0]

		cv2.imwrite('superPixel.png', img)


img = cv2.imread(sys.argv[1])
h, w = img.shape[:2]
img = cv2.resize(img, int(w/10), int(h/10)))
super(img)
