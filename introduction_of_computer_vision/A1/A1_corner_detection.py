import cv2 as cv
import matplotlib.pyplot as plt
import time
from A1.A1_function import *

img_lenna = cv.imread("lenna.png", cv.IMREAD_GRAYSCALE)
filter = get_gaussian_filter_2d(7,1.5)
img1 = cross_correlation_2d(img_lenna, filter)

img_shapes = cv.imread("shapes.png", cv.IMREAD_GRAYSCALE)
filter = get_gaussian_filter_2d(7,1.5)
img2 = cross_correlation_2d(img_shapes, filter)

def compute_corner_response( img ):
    img_sobel_x, img_sobel_y = get_sobel_img(img)
    IxIx = img_sobel_x * img_sobel_x
    IyIy = img_sobel_y * img_sobel_y
    IxIy = img_sobel_x * img_sobel_y

    window_size = 5
    offset = int(window_size/2)
    r = np.zeros(img.shape)
    for i in range(offset, img.shape[0]-offset):
        for j in range(offset, img.shape[1]-offset):
            window_IxIx = IxIx[i-offset:i+offset+1, j-offset:j+offset+1]
            window_IyIy = IyIy[i-offset:i+offset+1, j-offset:j+offset+1]
            window_IxIy = IxIy[i-offset:i+offset+1, j-offset:j+offset+1]
            Mxx = window_IxIx.sum()
            Myy = window_IyIy.sum()
            Mxy = window_IxIy.sum()
            det = Mxx*Myy - Mxy*Mxy
            trace = Mxx + Myy
            r[i,j] = det - 0.04 * (trace ** 2)
            if r[i,j]<0:
                r[i,j]=0
    max_r=np.max(r)
    r = np.divide(r, max_r)
    return r

def non_maximum_suppression_win( R, winsize ):
    center = int(winsize / 2)
    for i in range(center, R.shape[0] - center):
        for j in range(center, R.shape[1] - center):
            current_R = R[i - center:i + center, j - center:j + center]
            Rmax = current_R.max()
            if current_R[center][center] != Rmax:
                R[i][j] = 0
            if current_R[center][center] < 0.1:
                R[i][j] = 0
    return R

start=time.time()
R_lenna = compute_corner_response(img1)
end=time.time()
print("compute lenna corner response time : ", end-start)
cv.imshow("R_lenna",R_lenna)
cv.waitKey(3000)
plt.imsave("./result/part_3_corner_raw_lenna.png",R_lenna,cmap='gray')

start=time.time()
R_shapes = compute_corner_response(img2)
end=time.time()
print("compute shapes corner response time : ", end-start)
cv.imshow("R_shapes",R_shapes)
cv.waitKey(3000)
plt.imsave("./result/part_3_corner_raw_shapes.png",R_shapes,cmap='gray')

def change2green(img, R):
    img2color=np.empty((img.shape[0],img.shape[1],3))
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            for k in range(3):
                img2color[h][w][k]=img[h][w]
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            if R[h][w]>0.1:
                img2color[h][w][1]=255
    return img2color

def draw_circle(img, R):
    img2color=np.empty((img.shape[0],img.shape[1],3))
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            for k in range(3):
                img2color[h][w][k]=img[h][w]
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            if R[h][w]>0.1:
                for k in range(-1,2,1):
                    img2color[h-5][w+k]=[0,255,0]
                    img2color[h+k][w+5]=[0,255,0]
                    img2color[h+5][w+k]=[0,255,0]
                    img2color[h+k][w-5]=[0,255,0]
                    img2color[h - 4][w + k] = [0, 255, 0]
                    img2color[h + k][w + 4] = [0, 255, 0]
                    img2color[h + 4][w + k] = [0, 255, 0]
                    img2color[h + k][w - 4] = [0, 255, 0]
                    img2color[h+k+3][w-k+3]=[0,255,0]
                    img2color[h-k-3][w-k+3]=[0,255,0]
                    img2color[h+k+3][w+k-3]=[0,255,0]
                    img2color[h-k-3][w+k-3]=[0,255,0]
                for x in range(2,6,1):
                    img2color[h-x][w - x + 7] = [0, 255, 0]
                    img2color[h + x][w - x + 7] = [0, 255, 0]
                    img2color[h - x][w + x - 7] = [0, 255, 0]
                    img2color[h + x][w + x - 7] = [0, 255, 0]

    return img2color

lenna2color=change2green(img_lenna, R_lenna)
lenna2color = lenna2color.astype(np.uint8)
cv.imwrite("../A2/result/part_3_corner_bin_lenna.png", lenna2color)
cv.imshow("shapes2color",lenna2color)
cv.waitKey(3000)

shapes2color=change2green(img_shapes, R_shapes)
shapes2color = shapes2color.astype(np.uint8)
cv.imwrite("../A2/result/part_3_corner_bin_shapes.png", shapes2color)
cv.imshow("shapes2color",shapes2color)
cv.waitKey(3000)

start=time.time()
NMS_lenna=non_maximum_suppression_win(R_lenna, 11)
end=time.time()
print("compute lenna NMS time : ", end-start)
NMS_lenna2color = draw_circle(img_lenna, R_lenna)
cv.imwrite("../A2/result/part_3_corner_sup_lenna.png", NMS_lenna2color)
cv.imshow("lenna2color",NMS_lenna2color)
cv.waitKey(3000)

start=time.time()
NMS_shapes=non_maximum_suppression_win(R_shapes, 11)
end=time.time()
print("compute shapes NMS time : ", end-start)
NMS_shapes2color = draw_circle(img_shapes, R_shapes)
cv.imwrite("../A2/result/part_3_corner_sup_shapes.png", NMS_shapes2color)
cv.imshow("shapes2color",NMS_shapes2color)
cv.waitKey(3000)
