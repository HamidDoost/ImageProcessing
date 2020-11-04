'''
=============================================================================
-- Author:		Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 05/11/2020
-- Description:	This code is for drawing and extractig Convex Hull contour. 
                Convex Hull Contour is a connected contour.
-- Status:      In progress
==============================================================================

'''

import cv2
import sys
import imutils
import numpy as np

'''
saliancy
'''
saliency = cv2.saliency.StaticSaliencyFineGrained_create()
color = (0, 0, 255)


def saliantMap(image):
    (success, saliencyMap) = saliency.computeSaliency(image)
    saliencyMap = (saliencyMap * 255).astype("uint8")
    threshMap = cv2.threshold(saliencyMap, 0, 255,
                              cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    return threshMap


def convexHullfunction(image, threshMap):

    image = imutils.resize(image, width=int(
        image.shape[1]/8), height=int(image.shape[2]/8))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray, (3, 3))
    ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    hull = []

    for i in range(len(contours)):
        hull.append(cv2.convexHull(contours[i], False))
        drawing = np.zeros((threshMap.shape[0], thresh.shape[1], 3), np.uint8)

    for i in range(len(contours)):
        cv2.drawContours(drawing, hull, i, color, 1, 8)[2]
    cv2.imshow("Image", drawing)
    cv2.waitKey(0)
    for c in hull:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.2 * peri, True)

        screenCnt = approx
        print("STEP 2: Find contours of paper")
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("Outline", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


nn = 0.1
image = cv2.imread(sys.argv[1])
imagePath = sys.argv[1]
filename = imagePath.split("\\")[-1]

ho, wo = image.shape[:2]
ar = wo/ho
if ar < 1:
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
ho, wo = image.shape[:2]

ho, wo = image.shape[:2]

orig = image
threshMap = saliantMap(image)
convexHullfunction(image, threshMap)
