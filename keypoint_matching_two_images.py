'''
============================================================
-- Author:      Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 05/11/2020
-- Description:	This code is for keypoint matching between two files
-- Status:      In progress
=============================================================

'''


def akaze_match(im1, im2):
    # im1 = cv2.imread(im1_path)
    # im2 = cv2.imread(im2_path)
    hb, wb = im1.shape[:2]
    im1 = cv2.resize(im1, (int(wb/10), int(hb/10)))
    ha, wa = im2.shape[:2]
    im2 = cv2.resize(im2, (int(wa/10), int(ha/10)))

    gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    detector = cv2.AKAZE_create()
    (kps1, descs1) = detector.detectAndCompute(gray1, None)
    (kps2, descs2) = detector.detectAndCompute(gray2, None)

    print("keypoints: {}, descriptors: {}".format(len(kps1), descs1.shape))
    print("keypoints: {}, descriptors: {}".format(len(kps2), descs2.shape))

    # Match the features
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.knnMatch(descs1, descs2, k=2)

    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.9*n.distance:
            good.append([m])
    return(np.abs(chi2_distance(descs1, descs2)))
