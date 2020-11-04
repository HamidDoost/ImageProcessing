'''
SALIANCY detection
'''
import sys
import os
import cv2
import cv2
import os
import sys
saliency1 = cv2.saliency.StaticSaliencySpectralResidual_create()


def saliantMap1(image):
    (success, saliencyMap) = saliency1.computeSaliency(image)
    saliencyMap = (saliencyMap * 255).astype("uint8")
    threshMap = cv2.threshold(saliencyMap, 127, 255,
                              cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    return threshMap, saliencyMap


'''
saliancy
'''
saliency2 = cv2.saliency.StaticSaliencyFineGrained_create()


def saliantMap2(image):
    (success, saliencyMap) = saliency2.computeSaliency(image)
    saliencyMap = (saliencyMap * 255).astype("uint8")
    threshMap = cv2.threshold(saliencyMap, 0, 255,
                              cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imshow("saliencyMap.jpg", saliencyMap)
    cv2.imshow("threshMap.jpg", threshMap)
    cv2.waitKey(0)
    return threshMap, saliencyMap


image = cv2.imread(sys.argv[1])
ho, wo = image.shape[:2]
img = cv2.resize(image, (int(wo/10), int(ho/10)))
threshMap, saliencyMap = saliantMap1(img)
cv2.imshow('MASK', threshMap)
cv2.imshow('SALIANT', saliencyMap)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
