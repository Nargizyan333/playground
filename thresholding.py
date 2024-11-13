import cv2 as cv
import numpy as np

img = cv.imread("./img/sunflowers.png", cv.IMREAD_GRAYSCALE)

thresh = 0
max_value = 255

th, dst = cv.threshold(img, thresh, max_value, cv.THRESH_BINARY)
cv.imshow("THRESH_BINARY", dst)
cv.waitKey(0)
cv.destroyAllWindows()

th, dst = cv.threshold(img, thresh, max_value, cv.THRESH_BINARY_INV)
cv.imshow("THRESH_BINARY_INV", dst)
cv.waitKey(0)
cv.destroyAllWindows()

th, dst = cv.threshold(img, thresh, max_value, cv.THRESH_TRUNC)
cv.imshow("THRESH_TRUNC", dst)
cv.waitKey(0)
cv.destroyAllWindows()

th, dst = cv.threshold(img, thresh, max_value, cv.THRESH_TOZERO)
cv.imshow("THRESH_TOZERO", dst)
cv.waitKey(0)
cv.destroyAllWindows()

th, dst = cv.threshold(img, thresh, max_value, cv.THRESH_TOZERO_INV)
cv.imshow("THRESH_TOZERO_INV", dst)
cv.waitKey(0)
cv.destroyAllWindows()
