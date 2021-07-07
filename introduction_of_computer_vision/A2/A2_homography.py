import cv2
import numpy as np
import time
import random


def compute_homography( srcP, destP ):
    tildas, tildad, Mt1, Mt2, Ms1, Ms2 = normalize( srcP, destP )
    u, s, v = svd(tildas, tildad)
    s_num = np.argmin(s)
    HN = v[s_num].reshape(3, 3)
    TS = np.dot(Ms1, Mt1)
    TD_1 = np.linalg.inv(np.dot(Ms2, Mt2))
    H = np.dot(TD_1, np.dot(HN, TS))
    H = H/H[2][2]
    return H

def compute_homography_ransac ( srcP , destP , th ):
    inliers = []
    max_in = 0
    start, end = time.time(), time.time()
    while end - start <= 3:
        random_num=sorted(random.sample([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],10))
        randoms = np.float32([srcP[i] for i in random_num])
        randomd = np.float32([destP[i] for i in random_num])

        curr_H = compute_homography(randoms, randomd)
        reprojection = np.dot(curr_H, srcP.T).T
        error = np.array([np.sqrt((randomd[i][0] - reprojection[i][0]) ** 2 + (randomd[i][1] - reprojection[i][1]) ** 2) for i in range(len(randomd))])

        th2 = [th[i] for i in random_num]
        num = np.sum(error < th2)

        if num >= 6:
            for i in random_num :
                if i not in inliers:
                    inliers.append(i)
            if num >= max_in :
                H = curr_H
                max_in = num
                for i in random_num:
                    if i not in inliers:
                        inliers.append(i)
        end = time.time()

    idx = sorted(inliers)
    srcP_in, destP_in = [srcP[i] for i in idx], [destP[i] for i in idx]
    H = compute_homography(srcP_in, destP_in)
    return H

def findMatch(des1, des2, k):
    compare = np.array([])
    for i in range(len(des1)):
        nums=np.array([])
        for j in range(len(des2)):
            num=np.count_nonzero(des1[i] != des2[j])
            nums=np.append(nums, num)
        compare = np.append(compare, nums)
    sort_compare = np.argsort(compare)
    matchs=np.array([])

    for match in sort_compare:
        m1 = int(match // 500)
        m2 = int(match % 500)
        dis=compare[match]
        matchs= np.append(matchs, cv2.DMatch(m1, m2, 0, dis))
        matchs = matchs[:k]
    srcP = np.asarray([kp1[matchs[i].queryIdx].pt for i in range(len(matchs))])
    destP = np.asarray([kp2[matchs[i].trainIdx].pt for i in range(len(matchs))])
    return matchs, srcP, destP

print("########################### 2 - 1 ##############################")
img1 = cv2.imread("cv_desk.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("cv_cover.jpg", cv2.IMREAD_GRAYSCALE)
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute( img1, None )
kp2, des2 = orb.detectAndCompute( img2, None )
matchs, srcP, destP = findMatch(des1, des2, 10)
img = cv2.drawMatches(img1, kp1, img2, kp2, matchs, None, flags=2)
cv2.imshow("2-1",img)
cv2.waitKey(3000)

def verify(srcP, destP, k, th_down, th_up):
    while True:
        idx = sorted(random.sample([x for x in range(40)], k))
        V_srcP, V_destP = np.asarray([srcP[i] for i in idx]), np.asarray([destP[i] for i in idx])
        ones = np.ones((V_srcP.shape[0], 1))
        V_srcP, V_destP = np.hstack((V_srcP, ones)), np.hstack((V_destP, ones))
        H = compute_homography(V_srcP, V_destP)
        errs = np.array([])
        for i in range(V_srcP.shape[0]):
            re = np.dot(H, V_srcP[i].T)
            error = abs(V_destP[i] - re)
            errs = np.append(errs, error)
        esum = np.sum(errs)
        if th_down <= esum <= th_up:
            break
    return V_srcP, V_destP

def normalize( srcP, destP ):
    destP = np.asarray(destP)
    srcP = np.asarray(srcP)
    xmean1, ymean1 = np.mean(srcP[:][0]), np.mean(srcP[:][1])
    xmean2, ymean2 = np.mean(destP[:][0]), np.mean(destP[:][1])
    Mt1, Mt2 = [[1, 0, -xmean1], [0, 1, -ymean1], [0, 0, 1]], [[1, 0, -xmean2], [0, 1, -ymean2], [0, 0, 1]]

    ts, td = np.array([0, 0, 0]), np.array([0, 0, 0])
    for i in range(srcP.shape[0]):
        ts1, td1 = np.dot(Mt1, srcP[i].T), np.dot(Mt2, destP[i].T)
        ts = np.vstack((ts, ts1.T))
        td = np.vstack((td, td1.T))
    ts, td = ts[1:, :], td[1:, :]
    maxdis1 = np.max([np.sqrt(x[0] ** 2 + x[1] ** 2) for x in ts])
    maxdis2 = np.max([np.sqrt(x[0] ** 2 + x[1] ** 2) for x in td])
    Ms1 = [[np.sqrt(2) / maxdis1, 0, 0], [0, np.sqrt(2) / maxdis1, 0], [0, 0, 1]]
    Ms2 = [[np.sqrt(2) / maxdis2, 0, 0], [0, np.sqrt(2) / maxdis2, 0], [0, 0, 1]]
    tildas, tildad = np.array([0, 0, 0]), np.array([0, 0, 0])
    for i in range(ts.shape[0]):
        ts1, td1 = np.dot(Ms1, ts[i].T), np.dot(Ms2, td[i].T)
        tildas = np.vstack((tildas, ts1.T))
        tildad = np.vstack((tildad, td1.T))
    tildas, tildad = tildas[1:, :], tildad[1:, :]
    return tildas, tildad, Mt1, Mt2, Ms1, Ms2

def svd(tildas, tildad):
    A = np.array([[-s[0], -s[1], -1, 0, 0, 0, s[0] * d[0], s[1] * d[0], d[0],
                   0, 0, 0, -s[0], -s[1], -1, s[0] * d[1], s[1] * d[1], d[1]]
                  for s, d in zip(tildas, tildad)]
                 ).reshape(tildas.shape[0] * 2, 9)
    u, s, v = np.linalg.svd(A)
    return u,s,v

img1 = cv2.imread("cv_cover.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("cv_desk.png", cv2.IMREAD_GRAYSCALE)
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute( img1, None )
kp2, des2 = orb.detectAndCompute( img2, None )

print("########################### 2 - 2 ##############################")

matchs, src, dest = findMatch( des1, des2, 40 )
print("verifing")
srcP, destP = verify(src, dest, 15, 1400, 1500)
print("compute_homograpy")
H = compute_homography( srcP, destP )
Himg = cv2.warpPerspective(img1, H, (img2.shape[1],img2.shape[0]))
Himg = Himg.astype(np.uint8)
cv2.imshow("2-2-1", Himg)
cv2.waitKey(3000)

copy = img2.copy()
for i in range(Himg.shape[0]):
    for j in range(Himg.shape[1]):
        if Himg[i][j] != 0 :
            copy[i][j] = Himg[i][j]
copy = copy.astype(np.uint8)
cv2.imshow("2-2-2", copy)
cv2.waitKey(3000)

print("########################### 2 - 3 ##############################")

print("verifing")
srcP, destP = verify( src, dest, 15 ,1400, 1500)
reprojection = np.dot(H, srcP.T).T
error_th = [np.sqrt((destP[i][0]-reprojection[i][0])**2 + (destP[i][1]-reprojection[i][1])**2) for i in range(destP.shape[0])]
print("start ransac")
bestH = compute_homography_ransac( srcP , destP , error_th )
print("end ransac")
Himg = cv2.warpPerspective(img1, bestH, (img2.shape[1],img2.shape[0]))
Himg = Himg.astype(np.uint8)
cv2.imshow("2-3-1", Himg)
cv2.waitKey(3000)

copy = img2.copy()
for i in range(Himg.shape[0]):
    for j in range(Himg.shape[1]):
        if Himg[i][j] != 0 :
            copy[i][j] = Himg[i][j]
copy = copy.astype(np.uint8)
cv2.imshow("2-3-2", copy)
cv2.waitKey(3000)

print("########################### 2 - 4 ##############################")

img = cv2.imread("cv_cover.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread("hp_cover.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1, dsize = (img.shape[1],img.shape[0]), interpolation = cv2.INTER_AREA)
img2 = cv2.imread("cv_desk.png", cv2.IMREAD_GRAYSCALE)

Himg = cv2.warpPerspective(img1, bestH, (img2.shape[1],img2.shape[0]))
Himg = Himg.astype(np.uint8)
cv2.imshow("2-4-1", Himg)
cv2.waitKey(3000)

copy = img2.copy()
for i in range(Himg.shape[0]):
    for j in range(Himg.shape[1]):
        if Himg[i][j] != 0 :
            copy[i][j] = Himg[i][j]
copy = copy.astype(np.uint8)
cv2.imshow("2-4-2", copy)
cv2.waitKey(3000)

print("########################### 2 - 5 ##############################")

img1 = cv2.imread("diamondhead-11.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("diamondhead-10.png", cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

matchs, src, dest = findMatch( des1, des2, 40 )
srcP, destP= verify(src, dest, 15, 400,500)
H_1 = compute_homography(srcP, destP)

reprojection = np.dot(H_1, srcP.T).T
th = [np.sqrt((destP[i][0]-reprojection[i][0])**2 + (destP[i][1]-reprojection[i][1])**2) for i in range(destP.shape[0])]
srcP, destP =np.asarray(srcP), np.asarray(destP)
print(srcP.shape)
H_2 = compute_homography_ransac(srcP, destP, th)
H_img = cv2.warpPerspective(img1, H_2, (img2.shape[1]+img1.shape[1], img2.shape[0]))

for i in range(img2.shape[1], H_img.shape[1]):
    if H_img[20][i] == 0:
        end = i
        break

H_img[0:img2.shape[0], 0:img2.shape[1]] = img2
Himg = H_img[0:img2.shape[0], 0:end]
cv2.imshow("2-5-1", Himg)
cv2.waitKey(3000)

def mask(img1,img2,num):
     offset = 30
     border = img1.shape[1] - 30
     mask = np.zeros((img2.shape[0], img2.shape[1]+img1.shape[1]))
     if num == 'left_image':
         mask[:, border - offset:border + offset ] = np.tile(np.linspace(1, 0, 2 * offset ).T, (img2.shape[0], 1))
         mask[:, :border - offset] = 1
     elif num =='right_image':
         mask[:, border - offset :border + offset ] = np.tile(np.linspace(0, 1, 2 * offset ).T, (img2.shape[0], 1))
         mask[:, border + offset:] = 1
     return mask

def blending(H,img1,img2):
    panorama1 = np.zeros((img2.shape[0], img2.shape[1]+img1.shape[1]))
    mask1 = mask(img1,img2, num='left_image')
    panorama1[0:img1.shape[0], 0:img1.shape[1]] = img1
    panorama1 *= mask1
    mask2 = mask(img1,img2, num='right_image')
    panorama2 = cv2.warpPerspective(img2, H, (img2.shape[1]+img1.shape[1], img2.shape[0]))*mask2
    result=panorama1+panorama2

    rows, cols = np.where(result[:, :] != 0)
    min_row, max_row = min(rows), max(rows) + 1
    min_col, max_col = min(cols), max(cols) + 1
    final_result = result[min_row:max_row, min_col:max_col]
    return final_result

Himg = blending(H_2, img2, img1)
Himg=Himg.astype(np.uint8)
cv2.imshow("2-5-2", Himg)
cv2.waitKey(3000)
cv2.destroyAllWindows()