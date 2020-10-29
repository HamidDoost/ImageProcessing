# This code skew or deskew using perspective transform based on having 4 coordinate values to address them


import numpy as np
import cv2
import imutils
import sys
import os


def order_points(pts):

    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect


def four_point_transform(image, pts):

    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped

# this part is for skewing the image based on the value of m or n. If m!=0 and n=0 then image will be skewed toward left or right. If n!=0 and m=0 then image will be skewed toward top and bottom. Please modify m and n in line 71 and 72 accordingly.


def trans(image, m, n):
    h, w = image.shape[:2]
    # Arguments m ,n are highly depndent on size and rotation of image and should be modified accordingly
    pts = np.array([(0, n), (w, n), (w-m, h), (m, h-n)], dtype="float32")
    warped = four_point_transform(image, pts)
    return warped


fileMode = "jpg"
for root, dirs, files in os.walk(sys.argv[1]):
    for filename in files:
        ext = filename[filename.rfind("."):].lower()
        fn = os.path.join(root, filename)
        imagePath = fn
        image = cv2.imread(imagePath)
        (h, w) = image.shape[:2]
       # you can resize your image in line 70 if you need to.
       # image = cv2.resize(image, (int(w/10), int(h/10)))
        m = -90
        n = 0
        (h, w) = image.shape[:2]
       # Arguments m ,n should be modified
        warped = trans(image, m, n)
        cv2.imwrite(filename, warped)
