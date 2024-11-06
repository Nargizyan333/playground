import cv2 as cv
import numpy as np

img = cv.imread('./img/sunflowers.png')

# Translation

M = np.float32([[1, 0, 100], [0, 1, 100]])
height, width = img.shape[:2]

cv.imshow("Translated", cv.warpAffine(img, M, (width, height)))

# Rotation

M = cv.getRotationMatrix2D(((width - 1)/2, (height - 1)/2), 90, 1)
cv.imshow("Rotated", cv.warpAffine(img, M, (width, height)))

# Affine Transformation

pts1 = np.float32([[100, 100], [100, height - 100], [width - 100, height - 100]])
pts2 = np.float32([[0, 0], [0, height], [width, height]])
M = cv.getAffineTransform(pts1, pts2)
cv.imshow("Affine", cv.warpAffine(img, M, (width, height)))
cv.waitKey(0)
cv.destroyAllWindows()

# Perspective Transformation

pts1 = np.float32([[100, 100], [100, height - 100], [width - 100, height - 100], [width - 100, 100]])
pts2 = np.float32([[0, 0], [0, height], [width, height], [width, 0]])
M = cv.getPerspectiveTransform(pts1, pts2)
cv.imshow("Perspective", cv.warpPerspective(img, M, (width, height)))
cv.waitKey(0)
cv.destroyAllWindows()

