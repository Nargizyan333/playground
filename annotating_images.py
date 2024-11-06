import cv2 as cv
import numpy as np

img = cv.imread("./img/sunflowers.png")
height, width = img.shape[:2]
cv.imshow("Original", img)
cv.waitKey(0)

img_ = img.copy()
p1 = (100, 100)
p2 = (400, 600)
center = (250, 350)
ellipse_center = (500, 800)
axis = (200, 75)
cv.line(img_, p1, p2, (255, 0, 0), 3)
cv.circle(img_, center, 50, (255, 0, 0), 3)
cv.circle(img_, center, 20, (0, 0, 255), -1)
cv.rectangle(img_, (300, 500), (400, 550), (0, 255, 255), -1)
cv.ellipse(img_, ellipse_center, axis, 0, 0, 360, (255, 255, 0), 3)
cv.putText(img_, "Sunflowers", (width // 2, 100), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)
cv.imshow("", img_)
cv.waitKey(0)

