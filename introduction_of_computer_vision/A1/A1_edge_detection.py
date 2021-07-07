import cv2 as cv
import time
from A1.A1_function import *

img1 = cv.imread("lenna.png", cv.IMREAD_GRAYSCALE)
filter = get_gaussian_filter_2d(7,1.5)
img1 = cross_correlation_2d(img1, filter)

img2 = cv.imread("shapes.png", cv.IMREAD_GRAYSCALE)
filter = get_gaussian_filter_2d(7,1.5)
img2 = cross_correlation_2d(img2, filter)

def compute_image_gradient(img):
    img_x, img_y = get_sobel_img(img)
    mag = np.hypot(img_x, img_y)
    mag = mag/mag.max()*255
    dir = np.arctan2(img_y, img_x)
    mag = mag.astype(np.uint8)
    return dir, mag

start=time.time()
dir_lenna, mag_lenna = compute_image_gradient(img1)
end=time.time()
cv.imwrite("../A2/result/part_2_edge_raw_lenna.png", mag_lenna)
print("compute_lenna_gradient time : ", end-start)
cv.imshow("lenna derivation", mag_lenna)
cv.waitKey(3000)

start=time.time()
dir_shapes, mag_shapes = compute_image_gradient(img2)
end=time.time()
cv.imwrite("../A2/result/part_2_edge_raw_shapes.png", mag_shapes)
print("compute_shapes_gradient time : ", end-start)
cv.imshow("shapes derivation", mag_shapes)
cv.waitKey(3000)

def non_maximum_suppression_dir(mag, dir):
    M, N = mag.shape
    Z = np.zeros((M, N), dtype=np.int32)
    angle = dir * 180. / np.pi
    angle[angle < 0] += 180
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            q, r = 255, 255
            if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                q = mag[i, j + 1]
                r = mag[i, j - 1]
            elif (22.5 <= angle[i, j] < 67.5):
                q = mag[i - 1, j - 1]
                r = mag[i + 1, j + 1]
            elif (67.5 <= angle[i, j] < 112.5):
                q = mag[i + 1, j]
                r = mag[i - 1, j]
            elif (112.5 <= angle[i, j] < 157.5):
                q = mag[i + 1, j - 1]
                r = mag[i - 1, j + 1]

            if (mag[i, j] >= q) and (mag[i, j] > r):
                Z[i, j] = mag[i, j]
            else:
                Z[i, j] = 0
    Z = Z.astype(np.uint8)
    return Z

start=time.time()
mag_lenna = non_maximum_suppression_dir(mag_lenna, dir_lenna)
end=time.time()
print("compute_lenna NMS time : ", end-start)
cv.imwrite("../A2/result/part_2_edge_sup_lenna.png", mag_lenna)
cv.imshow("lenna NMS", mag_lenna)
cv.waitKey(3000)

start=time.time()
mag_shapes = non_maximum_suppression_dir(mag_shapes, dir_shapes)
end=time.time()
print("compute_shapes NMS time : ", end-start)
cv.imwrite("../A2/result/part_2_edge_sup_shapes.png", mag_shapes)
cv.imshow("lenna NMS", mag_shapes)
cv.waitKey(3000)