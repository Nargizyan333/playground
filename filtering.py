import cv2 as cv
import numpy as np

img = cv.imread("./img/wood.jpg")

cv.imshow("Wood", img)

kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

blured = cv.filter2D(img, -1, kernel1)

cv.imshow("Blured1", blured)

kernel2 = np.ones((5, 5), np.float32) / 25
blured = cv.filter2D(img, -1, kernel2)

cv.imshow("Blured2", blured)

blured = cv.blur(img, ksize=(5, 5))
cv.imshow("Blured3", blured)

blured = cv.GaussianBlur(img, (5, 5), sigmaX=0, sigmaY=0)
cv.imshow("Gaussian Blured", blured)

blured = cv.medianBlur(img, 5)
cv.imshow("Median Blured", blured)

blured = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow("Bilateral Blured", blured)

cv.waitKey(0)
cv.destroyAllWindows()

# Sharpening

kernel3 = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])

sharpened = cv.filter2D(img, -1, kernel3)

cv.imshow("Sharpened", sharpened)
cv.waitKey(0)
cv.destroyAllWindows()