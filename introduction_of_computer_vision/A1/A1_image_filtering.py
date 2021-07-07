import cv2 as cv
from A1.A1_function import *
import math
import time

def cross_correlation_1d(img , kernel):
    pad_img = padding_1d(img, kernel)
    h, w = img.shape
    hh, ww = kernel.shape
    out = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            current_img = pad_img[i:i + hh, j:j + ww]
            out[i, j] = np.sum(current_img * kernel)
    return out

def cross_correlation_2d(img, kernel):
    pad_img = padding_2d(img, kernel)
    h, w = img.shape
    hh, ww = kernel.shape
    out = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            current_img = pad_img[i:i + hh, j:j + ww]
            out[i, j] = np.sum(current_img * kernel)
    return out

def get_gaussian_filter_1d(size, sigma):
    g_filter1 = np.zeros((1, size))
    for i in range(size):
        g_filter1[0, i] = (1 / np.sqrt(2 * math.pi * sigma)) * math.exp(
            -(pow(size // 2 - i, 2) / (2 * pow(sigma, 2))))
    sumf = g_filter1.sum()
    g_filter1 = g_filter1 / sumf
    return g_filter1

def get_gaussian_filter_2d(size, sigma):
    g_filter1 = get_gaussian_filter_1d(size, sigma)
    g_filter_2d = np.outer(g_filter1, g_filter1.T)
    return g_filter_2d

img=cv.imread("lenna.png", cv.IMREAD_GRAYSCALE)
diff=0
start=time.time()
filter=get_gaussian_filter_2d(5,1)
out1=cross_correlation_2d(img, filter)
middle=time.time()
print("2d gaussian filter : \n", filter)
print("lenna gaussian filter time : " , middle-start)

filter1=get_gaussian_filter_1d(5,1)
out2=cross_correlation_1d(img, filter1)
out2=cross_correlation_1d(img, filter1.T)
diff= np.sum(abs(out1-out2))
cv.imshow("lenna diffence map", abs(out1-out2).astype(np.uint8))
cv.waitKey(2000)
print("1d gaussian filter : ", filter1)
print(" lenna : 1d gaussian filter result - 2d gaussian filter result =" , diff)

size=[5,11,21]
sigma=[1,11,17]
outs=[]
for i in size:
    for j in sigma:
        filter = get_gaussian_filter_2d(i,j)
        out=cross_correlation_2d(img, filter)
        out=cv.resize(out,(0,0), fx=0.4,fy=0.4)
        cv.putText(out, "%dx%d s=%d"%(i,i,j), (10,20), 2, 0.5, 255)
        out = out.astype(np.uint8)
        outs.append(out)
out1 = np.hstack((outs[1],outs[1],outs[2]))
out2 = np.hstack((outs[3],outs[4],outs[5]))
out3 = np.hstack((outs[6],outs[7],outs[8]))
out = np.vstack((out1, out2, out3))
out = out.astype(np.uint8)
cv.imwrite("../A2/result/part_1_gaussian_filter_lenna.png", out)
cv.imshow("lenna",out)
cv.waitKey(2000)

img=cv.imread("shapes.png", cv.IMREAD_GRAYSCALE)
start=time.time()
filter=get_gaussian_filter_2d(5,1)
out1=cross_correlation_2d(img, filter)
middle=time.time()
print("shape gaussian filter time : " , middle-start)

filter1=get_gaussian_filter_1d(5,1)
out2=cross_correlation_1d(img, filter1)
out2=cross_correlation_1d(img, filter1.T)
diff= np.sum(abs(out1-out2))
cv.imshow("shapes diffence map", abs(out1-out2).astype(np.uint8))
cv.waitKey(2000)
print(" shape : 1d gaussian filter result - 2d gaussian filter result =" , diff)

outs=[]
for i in size:
    for j in sigma:
        filter = get_gaussian_filter_2d(i,j)
        out=cross_correlation_2d(img, filter)
        out=cv.resize(out,(0,0), fx=0.4,fy=0.4)
        cv.putText(out, "%dx%d s=%d"%(i,i,j), (10,12), 2, 0.5, 0)
        out = out.astype(np.uint8)
        outs.append(out)
out1 = np.hstack((outs[1],outs[1],outs[2]))
out2 = np.hstack((outs[3],outs[4],outs[5]))
out3 = np.hstack((outs[6],outs[7],outs[8]))
out = np.vstack((out1, out2, out3))
out = out.astype(np.uint8)
cv.imwrite("../A2/result/part_1_gaussian_filter_shape.png", out)
cv.imshow("shape",out)
cv.waitKey(2000)
cv.destroyAllWindows()