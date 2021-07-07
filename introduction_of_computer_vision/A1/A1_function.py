import numpy as np
import math

def padding_2d(img,kernel):
    x, y = kernel.shape
    pad_h = int((x - 1) / 2)
    pad_w = int((y - 1) / 2)

    patch_h1 = img[:, 0].reshape(img.shape[0], 1)
    patch_h2 = img[:, -1].reshape(img.shape[0], 1)

    for i in range(pad_w):
        img = np.hstack((patch_h1, img))
        img = np.hstack((img, patch_h2))

    patch_w1 = img[0, :].reshape(1, img.shape[1])
    patch_w2 = img[-1, :].reshape(1, img.shape[1])

    for i in range(pad_h):
        img = np.vstack((patch_w1, img))
        img = np.vstack((img, patch_w2))
    return img

def padding_1d(img, kernel):
    x,y=kernel.shape
    pad_h = int((x - 1) / 2)
    pad_w = int((y - 1) / 2)
    patch_h1 = img[:, 0].reshape(img.shape[0], 1)
    patch_h2 = img[:, -1].reshape(img.shape[0], 1)
    patch_w1 = img[0, :]
    patch_w2 = img[-1, :]

    if (pad_h == 0) :
        left, right = np.zeros((img.shape[0], pad_w)), np.zeros((img.shape[0], pad_w))
        left = left + patch_h1
        right = right + patch_h2
        img = np.hstack((left, img, right))

    elif (pad_w == 0):
        bottom, top = np.zeros((pad_h, img.shape[1])), np.zeros((pad_h, img.shape[1]))
        bottom = bottom + patch_w2
        top = top + patch_w1
        img = np.vstack((top, img, bottom))
    return img

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

def get_sobel_img(img):
    derivate = np.array([-1,0,1]).reshape(1, 3)
    gaussian = np.array([1,2,1]).reshape(1, 3)
    img_x = cross_correlation_2d(img, gaussian.T * derivate)
    img_y = cross_correlation_2d(img, derivate.T * gaussian)
    return img_x, img_y
