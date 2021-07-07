import numpy as np
import cv2
import random
import time
from CV_A3_2017310695.compute_avg_reproj_error import *
from CV_A3_2017310695.A3_functions import *

def compute_F_raw(M):
    A = np.array([[m[0] * m[2], m[0] * m[3], m[0], m[1] * m[2], m[1] * m[3], m[1], m[2], m[3], 1]
                  for m in M[:8]])
    u, s, v = np.linalg.svd(A)
    s_min = np.argmin(s)
    F = v[s_min].reshape(3,3)
    F/=F[2][2]
    return F

def compute_F_norm(M):
    ones = np.ones((M.shape[0], 1))
    M1, M2 = M[:, 0:2], M[:, 2:4]
    M1, M2 = np.hstack((M1, ones)), np.hstack((M2, ones))

    T1 = [[(2 / left.shape[1]), 0, -(2 / left.shape[1]) * (left.shape[1] / 2 - 0.5)],
          [0, (2 / left.shape[0]), -(2 / left.shape[0]) * (left.shape[0] / 2 - 0.5)],
          [0, 0, 1]]
    T2 = [[(2 / right.shape[1]), 0, -(2 / right.shape[1]) * (right.shape[1] / 2 - 0.5)],
          [0, (2 / right.shape[0]), -(2 / right.shape[0]) * (right.shape[0] / 2 - 0.5)],
          [0, 0, 1]]

    normM1s, normM2s = [0, 0, 0], [0, 0, 0]
    for i in range(8):
        normM1 = np.dot(T1, M1[i].T)
        normM2 = np.dot(T2, M2[i].T)
        normM1s = np.vstack((normM1s, normM1.T))
        normM2s = np.vstack((normM2s, normM2.T))
    normM1s, normM2s = normM1s[1:, 0:2], normM2s[1:, 0:2]
    M_norm = np.hstack((normM1s, normM2s))

    A = np.array([[m[0] * m[2], m[0] * m[3], m[0], m[1] * m[2], m[1] * m[3], m[1], m[2], m[3], 1]
                  for m in M_norm[:8]])
    u, s, v = np.linalg.svd(A)
    s_min = np.argmin(s)
    NF = v[s_min].reshape(3, 3)

    u, s, v = np.linalg.svd(NF)
    s_rank2 = [[s[0], 0, 0], [0, s[1], 0], [0, 0, 0]]
    NF = np.dot(u, np.dot(s_rank2, v))
    F = np.dot(np.array(T2).T, np.dot(NF,T1))
    F /= F[2][2]

    return F

def compute_F_mine(M):
    global small_err
    start, end = time.time(), time.time()
    while end - start <= 3:
        random_num = random.sample([i for i in range(0,M.shape[0])],8)
        random_M = np.array([M[i] for i in random_num]).reshape(8,4)
        random_F = compute_F_raw(random_M)
        random_err = compute_avg_reproj_error(random_M, random_F)
        if random_err <= small_err :
            best_F = random_F
            small_err = random_err
        end = time.time()
    return best_F




small_err = None
F_mine = None
def f_print(txt):
    global small_err, F_mine
    M = np.loadtxt(txt)
    M_delete = deleteM(M)

    F_raw = compute_F_raw(M_delete)
    err_raw = compute_avg_reproj_error(M_delete[20:28], F_raw)
    small_err = err_raw

    F_norm = compute_F_norm(M_delete)
    err_norm = compute_avg_reproj_error(M_delete[20:28], F_norm)

    F_mine = compute_F_mine(M_delete)
    err_mine = small_err
    print("     Raw = ", err_raw)
    print("     Norm = ", err_norm)
    print("     Mine = ", err_mine)
    print(" ")

def vis(name1, name2,txt):
    global F_mine
    while True:
        left = cv2.imread(name1, cv2.IMREAD_COLOR)
        right = cv2.imread(name2, cv2.IMREAD_COLOR)
        M = np.loadtxt(txt)
        M = deleteM(M)
        random_num = random.sample([i for i in range(0, M.shape[0])], 3)
        random_match = np.array([M[i] for i in random_num]).reshape(3, 4)

        # right point로 left image에 epipolar line
        lines1 = np.array([0, 0, 0])
        for i in range(3):
            line = np.dot(F_mine.T, [[random_match[i][2]], [random_match[i][3]], [1]])
            lines1 = np.vstack((lines1, line.T))
        lines1 = lines1[1:, :]
        left_epipolar = drawline(left, lines1)

        # left point로 right image에 epipolar line
        lines2 = np.array([0, 0, 0])
        for i in range(3):
            line = np.dot(F_mine, [[random_match[i][0]], [random_match[i][1]], [1]])
            lines2 = np.vstack((lines2, line.T))
        lines2 = lines2[1:, :]
        right_epipolar = drawline(right, lines2)

        color = ((255, 0, 0), (0, 255, 0), (0, 0, 255))
        for i in range(3):
            cv2.circle(left_epipolar, (int(random_match[i][2]), int(random_match[i][3])), 2, color[i], 2)
            cv2.circle(right_epipolar, (int(random_match[i][0]), int(random_match[i][1])), 2, color[i], 2)

        cv2.imshow('left', left_epipolar)
        cv2.imshow('right', right_epipolar)
        key = cv2.waitKey(0)

        if key == ord('q'):
            break

left = cv2.imread('temple1.png', cv2.IMREAD_GRAYSCALE)
right = cv2.imread('temple2.png', cv2.IMREAD_GRAYSCALE)
print("Average Reprojection Errors ( temple1.png and temple2.png )")
f_print( 'temple_matches.txt')
vis('temple1.png', 'temple2.png','temple_matches.txt')

left = cv2.imread('house1.jpg', cv2.IMREAD_GRAYSCALE)
right = cv2.imread('house2.jpg', cv2.IMREAD_GRAYSCALE)
print("Average Reprojection Errors ( house1.jpg and house2.jpg )")
f_print('house_matches.txt')
vis('house1.jpg', 'house2.jpg','house_matches.txt')

left = cv2.imread('library1.jpg', cv2.IMREAD_GRAYSCALE)
right = cv2.imread('library2.jpg', cv2.IMREAD_GRAYSCALE)
print("Average Reprojection Errors ( library1.jpg and library2.jpg )")
f_print('library_matches.txt')
vis('library1.jpg', 'library2.jpg','library_matches.txt')