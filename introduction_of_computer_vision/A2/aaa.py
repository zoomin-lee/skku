import numpy as np
import math
import cv2
import functions
import random
import time

##################### homography #######################
def compute_homography(srcP, destP): #(N,2)
    if NORMALIZATION == 1:
        srcP, TS = functions.src_normalization(srcP)
        destP, invTD = functions.dest_normalization(destP)
        n = srcP.shape[0]
        matA = np.array([[-s[0], -s[1], -1, 0, 0, 0, s[0] * d[0], s[1] * d[0], d[0],
                          0, 0, 0, -s[0], -s[1], -1, s[0] * d[1], s[1] * d[1], d[1]]
                         for s, d in zip(srcP, destP)]
                        ).reshape(n * 2, 9)

        U, s, Vt = np.linalg.svd(matA, full_matrices=True)
        HN = Vt.T[:, 8].reshape(3, 3)
        H = np.dot(invTD, np.dot(HN, TS))
        H /= H[2][2]

    elif NORMALIZATION == 0:
        srcP = functions.coor_change(srcP)
        destP = functions.coor_change(destP)
        n = srcP.shape[0]
        A = np.array([[-s[0], -s[1], -1, 0, 0, 0, s[0] * d[0], s[1] * d[0], d[0],
              0, 0, 0, -s[0], -s[1], -1, s[0] * d[1], s[1] * d[1], d[1]]
                         for s, d in zip(srcP, destP)]
                     ).reshape(n*2, 9)

        U, s, Vh = np.linalg.svd(A, full_matrices = True)
        H = Vh[8].reshape(3, 3)
        H /= H[2][2]

    return H


############### 2 - 2 homography with normalization ####################
"""
NORMALIZATION = 1

img1 = cv2.imread("cv_cover.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("cv_desk.png", cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
matches = functions.DMatches_Hamming(des1, des2)
sorted_matches = matches[:40]

srcP_N, destP_N = functions.getP(sorted_matches, kp1, kp2)
"""
def robust_alignment(srcP_1, destP_1, n):
    reference_error_u = 1500
    reference_error_b = 1400
    while True :
        ind = sorted(random.sample([x for x in range(40)], n))
        srcP, destP = [srcP_1[i] for i in ind], [destP_1[i] for i in ind]
        H = compute_homography(srcP, destP)
        reprojection = np.dot(H, functions.coor_change(srcP).T).T #(n,3)
        error = abs(functions.coor_change(destP) - reprojection)
        error_sum = np.sum(error)
        if error_sum < reference_error_u and error_sum > reference_error_b:
            break
    return srcP, destP

def robust_alignment2(srcP_N, destP_N, n):

    srcP = None
    destP = None
    min_error_sum = 100000
    ref = time.time()
    while True:
        ind = sorted(random.sample([x for x in range(len(srcP_N))], n))
        curr_srcP, curr_destP = [srcP_N[i] for i in ind], [destP_N[i] for i in ind]
        curr_H = compute_homography(curr_srcP, curr_destP)
        reprojection = np.dot(H_1, functions.coor_change(curr_srcP).T).T  # (n,3)
        error = abs(functions.coor_change(curr_destP) - reprojection)
        error_sum = np.sum(error)
        if error_sum < min_error_sum:
            srcP = curr_srcP
            destP = curr_destP
        if time.time()-ref >= 5 :
            break
    return srcP, destP
"""
srcP_1, destP_1 = robust_alignment(srcP_N,destP_N, 15)
H_1 = compute_homography(srcP_1, destP_1)
# HOMO_NORM = cv2.warpPerspective(img1, H_1, (img2.shape[1], img2.shape[0]))

# functions.showing(HOMO_NORM)
"""
def counting_inliers2(srcP2, destP2, th, random_comb):
    #th : error_mean
    curr_H = compute_homography(srcP2, destP2)
    reprojection = np.dot(curr_H, functions.coor_change(srcP2).T).T
    error = np.array([np.sqrt((destP2[i][0] - reprojection[i][0])**2 + (destP2[i][1]-reprojection[i][1])**2) for i in range(len(destP2))])

    th = [th[i] for i in random_comb]
    inliers_index = np.argwhere(error < th)
    inliers_cnt = np.sum(error<th)
    return curr_H, inliers_cnt, inliers_index

######################## 2 - 3 RANSAC############################

def thresholding(srcP, destP):
    reprojection = np.dot(H_1, functions.coor_change(srcP).T).T
    threshold = np.array([np.sqrt((destP[i][0] - reprojection[i][0])**2 + (destP[i][1]-reprojection[i][1])**2) for i in range(len(destP))])
    return threshold

NORMALIZATION = 0

def compute_homography_ransac2(srcP, destP, th, n):
    H = None
    inlier_indices = []
    max_inliers = 0
    ref = time.time()
    while True :
        random_comb = sorted(random.sample([x for x in range(len(srcP))], n))
        srcP2, destP2 = [srcP[i] for i in random_comb], [destP[i] for i in random_comb]
        curr_H, inlier_cnt, inlier_index = counting_inliers2(srcP2, destP2, th, random_comb)
        if inlier_cnt >= 4:
            for i in random_comb :
                if i not in inlier_indices:
                    inlier_indices.append(i)
            if inlier_cnt >= max_inliers :
                H = curr_H
                max_inliers = inlier_cnt
                for i in random_comb:
                    if i not in inlier_indices:
                        inlier_indices.append(i)

        if time.time()-ref >= 3:
            print("time overlapped: ",time.time()-ref)
            break
    print("max inlier 개수 : ", max_inliers)
    inlier_indices = sorted(inlier_indices)
    print("used index from matches : \n", inlier_indices)
    srcP_in, destP_in = [srcP[i] for i in inlier_indices], [destP[i] for i in inlier_indices]
    H = compute_homography(srcP_in, destP_in)

    return H


NORMALIZATION = 0

##################################################

# 40개의 sorted matche에 대해 ROBUST ALIGNMENT로 N1개를 뽑고
# 그 중 N2개의 조합으로 RANSAC 진행

# img1 = cv2.imread("cv_cover.jpg", cv2.IMREAD_GRAYSCALE)
# img2 = cv2.imread("cv_desk.png", cv2.IMREAD_GRAYSCALE)
# srcP_standard, destP_standard = functions.getP(sorted_matches, kp1, kp2) #40개
# srcP_ROBUST, destP_ROBUST = robust_alignment2(srcP_standard, destP_standard, 30)
# threshold = thresholding(srcP_ROBUST, destP_ROBUST)
#
# H = compute_homography_ransac2(srcP_ROBUST, destP_ROBUST, threshold, 8)
# res = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))
# functions.showing(res)

##############################################################

# 2-2 에서 ROBUST로 구한 SRC, DEST 그대로 사용하여
# N개의 조합 뽑아서 RANSAC

# th = thresholding(srcP_1, destP_1)
# H = compute_homography_ransac2(srcP_1, destP_1, th, 4)
# res = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))
# functions.showing(res)


#################### ROBUST 사용 2 #############################
############### 40개 >> N1개 >> N2 개 추출 #######################

##########잘 안됨 ##############
# srcP_40, destP_40 = functions.getP(sorted_matches, kp1, kp2)
# srcP_N1, destP_N1 = robust_alignment2(srcP_40, destP_40, 15)
# th = thresholding(srcP_N1, destP_N1, H_1)
# H = compute_homography_ransac2(srcP_N1, destP_N1, th, 4)
# res = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))
# cv2.imshow("ROBUST_RANSAC", res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



################## 2 - 4 ###################
"""
img1 = cv2.imread("cv_cover.jpg", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("hp_cover.jpg", cv2.IMREAD_GRAYSCALE)

new_hp_cover = cv2.resize(img3, dsize = (img1.shape[1],img1.shape[0]), interpolation = cv2.INTER_AREA)
result = cv2.warpPerspective(new_hp_cover, H, (img2.shape[1],img2.shape[0]))
# cv2.imshow("result", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img2 = cv2.imread("cv_desk.png", cv2.IMREAD_GRAYSCALE)
composed = img2.copy()
for i in range(result.shape[0]):
    for j in range(result.shape[1]):
        if result[i][j] != 0 :
            composed[i][j] = result[i][j]
composed = composed.astype(np.uint8)
cv2.imshow("HP_COMPOSED", composed)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""