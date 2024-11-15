import cv2 as cv
import numpy as np

img = cv.imread("./img/test.jpg")

cv.imshow("Original", img)
cv.waitKey(0)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(img_gray, (3, 3), 0)

# Sobel Edge Detection
sobel_x = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
sobel_y = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
sobel_xy = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)

cv.imshow('Sobel X', sobel_x)
cv.waitKey(0)
cv.imshow('Sobel Y', sobel_y)
cv.waitKey(0)
cv.imshow('Sobel X Y using Sobel() function', sobel_xy)
cv.waitKey(0)

edges = cv.Canny(image=img_blur, threshold1=100, threshold2=200)
cv.imshow('Canny Edge Detection', edges)
cv.waitKey(0)

cv.destroyAllWindows()