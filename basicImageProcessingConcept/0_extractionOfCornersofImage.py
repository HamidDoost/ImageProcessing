'''
corners
'''
import cv2
import sys
import os
import numpy as np

imagepath = sys.argv[1]
image = cv2.imread(imagepath)

# sobelCombined can be used from SobelXYAndLaplacian or from SaliencyThresshold or ordinary treshold
corners = cv2.goodFeaturesToTrack(sobelCombined, 25, 0.01, 10)
corners = np.int0(corners)
xs = []
ys = []
for i in corners:
    x, y = i.ravel()
    cv2.circle(image, (x, y), 3, 255, -1)

    xs.append(x)
    ys.append(y)

x0 = min(xs)
y0 = min(ys)
x1 = max(xs)
y1 = max(ys)
print(x0, x1, y0, y1)
image = image[y0:y1]
