#!/usr/bin/env python
# coding: UTF-8
# author: Dc Zheng time:2019/12/29


from skimage.measure import compare_ssim, compare_psnr
import numpy as np
import cv2

img1 = cv2.imread('D:/img_002_SRF.png')  # 读取图像
img2 = cv2.imread('x2.5_SR.png')  # 读取图像

img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))

print(img2.shape)

print(img1.shape)

ssim = compare_ssim(img1, img2, multichannel=True)
psnr = compare_psnr(img1, img2, 255)
print(ssim, psnr)



